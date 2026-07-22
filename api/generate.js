// Takeover Studio → Higgsfield proxy (Vercel serverless function).
//
// Public-facing: this endpoint will serve Takeover Conquest users generating
// promo lore, so it ships with strict abuse protection:
//   • same-origin only (Origin/Referer must match the deployment host, or ALLOWED_ORIGINS)
//   • optional access code gate (STUDIO_ACCESS_CODE env → client sends x-access-code)
//   • strict rate limits per IP and per instance (in-memory, best-effort on
//     serverless — swap in Vercel KV for hard global caps when traffic grows)
//   • prompt validation + aspect-ratio allowlist, one image per request
//
// Env vars (Vercel → Project → Settings → Environment Variables):
//   HIGGSFIELD_API_KEY  required  "KEY_ID:KEY_SECRET" from platform.higgsfield.ai
//   HIGGSFIELD_MODEL    optional  model path (default nano-banana/text-to-image)
//   HIGGSFIELD_BASE     optional  API base (default https://platform.higgsfield.ai)
//   STUDIO_ACCESS_CODE  optional  if set, requests must send matching x-access-code
//   ALLOWED_ORIGINS     optional  comma-separated extra allowed origins

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/* ---------------- rate limiting (in-memory, per warm instance) ---------------- */
const LIMITS = {
  ipPerMin: 4,      // per-IP requests / minute
  ipPerHour: 20,    // per-IP requests / hour
  ipPerDay: 40,     // per-IP requests / day
  ipConcurrent: 2,  // per-IP in-flight
  globalPerMin: 12, // per-instance requests / minute
  globalPerDay: 300,// per-instance requests / day
  globalConcurrent: 4,
};
const buckets = new Map(); // ip -> {min:[], hour:[], day:[], inflight}
const globalB = { min: [], day: [], inflight: 0 };

function prune(arr, windowMs, now) {
  while (arr.length && now - arr[0] > windowMs) arr.shift();
}
function checkLimits(ip) {
  const now = Date.now();
  if (buckets.size > 5000) buckets.clear(); // memory guard
  let b = buckets.get(ip);
  if (!b) { b = { min: [], hour: [], day: [], inflight: 0 }; buckets.set(ip, b); }
  prune(b.min, 60e3, now); prune(b.hour, 3600e3, now); prune(b.day, 86400e3, now);
  prune(globalB.min, 60e3, now); prune(globalB.day, 86400e3, now);

  if (b.inflight >= LIMITS.ipConcurrent) return { ok: false, retry: 15, why: 'too many generations in flight' };
  if (globalB.inflight >= LIMITS.globalConcurrent) return { ok: false, retry: 20, why: 'server busy' };
  if (b.min.length >= LIMITS.ipPerMin) return { ok: false, retry: 60, why: 'per-minute limit' };
  if (b.hour.length >= LIMITS.ipPerHour) return { ok: false, retry: 900, why: 'hourly limit' };
  if (b.day.length >= LIMITS.ipPerDay) return { ok: false, retry: 3600, why: 'daily limit' };
  if (globalB.min.length >= LIMITS.globalPerMin) return { ok: false, retry: 60, why: 'server per-minute limit' };
  if (globalB.day.length >= LIMITS.globalPerDay) return { ok: false, retry: 3600, why: 'server daily limit' };

  b.min.push(now); b.hour.push(now); b.day.push(now);
  globalB.min.push(now); globalB.day.push(now);
  b.inflight++; globalB.inflight++;
  return { ok: true, done: () => { b.inflight = Math.max(0, b.inflight - 1); globalB.inflight = Math.max(0, globalB.inflight - 1); } };
}

/* ---------------- validation ---------------- */
const AR_ALLOWED = new Set(['1:1', '3:4', '4:3', '16:9', '9:16', '2:3', '3:2']);
function validate(body) {
  const prompt = (body.prompt || '').toString().trim();
  if (!prompt) return { err: 'prompt required' };
  if (prompt.length > 2500) return { err: 'prompt too long (max 2500 chars)' };
  if (/data:[a-z]+\//i.test(prompt)) return { err: 'inline data not allowed in prompt' };
  const aspect_ratio = (body.aspect_ratio || '3:4').toString();
  if (!AR_ALLOWED.has(aspect_ratio)) return { err: 'aspect_ratio not allowed' };
  let seed;
  if (body.seed != null) { seed = Number(body.seed); if (!Number.isFinite(seed)) return { err: 'bad seed' }; }
  return { prompt, aspect_ratio, seed };
}

function originAllowed(req) {
  const host = (req.headers['x-forwarded-host'] || req.headers.host || '').toString().split(',')[0].trim().toLowerCase();
  const extra = (process.env.ALLOWED_ORIGINS || '').split(',').map(s => s.trim().toLowerCase()).filter(Boolean);
  const src = (req.headers.origin || req.headers.referer || '').toString().toLowerCase();
  if (!src) return false; // browsers always send Origin/Referer on fetch POST; bare curl does not
  let srcHost = '';
  try { srcHost = new URL(src).host.toLowerCase(); } catch { return false; }
  if (host && srcHost === host) return true;
  return extra.some(o => { try { return new URL(o.startsWith('http') ? o : 'https://' + o).host === srcHost; } catch { return o === srcHost; } });
}

function clientIp(req) {
  return ((req.headers['x-forwarded-for'] || '').toString().split(',')[0].trim()) || req.socket?.remoteAddress || 'unknown';
}

/* ---------------- higgsfield ---------------- */
function pickImage(j) {
  if (!j || typeof j !== 'object') return null;
  if (Array.isArray(j.images) && j.images[0]) return j.images[0].url || j.images[0].raw?.url || null;
  if (Array.isArray(j.jobs) && j.jobs[0]?.results) {
    const r = j.jobs[0].results;
    return r.raw?.url || r.min?.url || r.url || null;
  }
  if (j.result?.images?.[0]) return j.result.images[0].url || null;
  if (j.output?.[0]?.url) return j.output[0].url;
  if (j.raw?.url) return j.raw.url;
  if (typeof j.url === 'string') return j.url;
  return null;
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'POST only' });

  // --- gates ---
  if (!originAllowed(req)) return res.status(403).json({ error: 'origin not allowed' });
  const CODE = process.env.STUDIO_ACCESS_CODE;
  if (CODE && (req.headers['x-access-code'] || '') !== CODE) {
    return res.status(401).json({ error: 'access code required' });
  }

  const KEY = process.env.HIGGSFIELD_API_KEY;
  if (!KEY) return res.status(500).json({ error: 'HIGGSFIELD_API_KEY not set in Vercel env' });

  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch { body = {}; } }
  const v = validate(body || {});
  if (v.err) return res.status(400).json({ error: v.err });

  // --- rate limit ---
  const rl = checkLimits(clientIp(req));
  if (!rl.ok) {
    res.setHeader('Retry-After', String(rl.retry));
    return res.status(429).json({ error: 'rate limited: ' + rl.why, retry_after: rl.retry });
  }

  const BASE = (process.env.HIGGSFIELD_BASE || 'https://platform.higgsfield.ai').replace(/\/$/, '');
  const MODEL = (process.env.HIGGSFIELD_MODEL || 'nano-banana/text-to-image').replace(/^\//, '');
  const auth = { Authorization: 'Key ' + KEY, 'Content-Type': 'application/json' };
  const input = { prompt: v.prompt, aspect_ratio: v.aspect_ratio, ...(v.seed != null ? { seed: v.seed } : {}) };

  try {
    const sub = await fetch(`${BASE}/${MODEL}`, { method: 'POST', headers: auth, body: JSON.stringify(input) });
    const subJson = await sub.json().catch(() => ({}));
    if (!sub.ok) return res.status(502).json({ error: `Higgsfield submit ${sub.status}`, detail: subJson });

    let img = pickImage(subJson);
    if (img) return res.status(200).json({ image: img });

    const reqId = subJson.request_id || subJson.id;
    const statusUrl = subJson.status_url || (reqId ? `${BASE}/requests/${reqId}/status` : null);
    const responseUrl = subJson.response_url || (reqId ? `${BASE}/requests/${reqId}` : null);
    if (!statusUrl) return res.status(502).json({ error: 'no request id / status url from Higgsfield', detail: subJson });

    for (let i = 0; i < 45; i++) {
      await sleep(2000);
      const st = await fetch(statusUrl, { headers: auth });
      const sj = await st.json().catch(() => ({}));
      img = pickImage(sj);
      if (img) return res.status(200).json({ image: img });
      const status = (sj.status || '').toLowerCase();
      if (status === 'completed' || status === 'succeeded') {
        if (responseUrl) {
          const rr = await fetch(responseUrl, { headers: auth });
          const rj = await rr.json().catch(() => ({}));
          img = pickImage(rj);
          if (img) return res.status(200).json({ image: img });
          return res.status(502).json({ error: 'completed but no image found', detail: rj });
        }
        return res.status(502).json({ error: 'completed but no image found', detail: sj });
      }
      if (status === 'failed' || status === 'nsfw' || status === 'canceled') {
        return res.status(502).json({ error: 'Higgsfield job ' + status });
      }
    }
    return res.status(504).json({ error: 'Higgsfield timed out' });
  } catch (e) {
    return res.status(500).json({ error: 'proxy error: ' + (e && e.message || e) });
  } finally {
    rl.done();
  }
};
