// Takeover Studio → Higgsfield proxy (Vercel serverless function).
//
// Keeps the Higgsfield API key server-side (browser calls to the Higgsfield API
// are blocked). The studio POSTs { prompt, aspect_ratio } here; we submit to the
// Higgsfield Cloud API, poll until the job completes, and return { image: url }.
//
// Required env var (Vercel → Project → Settings → Environment Variables):
//   HIGGSFIELD_API_KEY = "KEY_ID:KEY_SECRET"   (create at https://platform.higgsfield.ai)
// Optional:
//   HIGGSFIELD_MODEL   = model path/id to submit to (default below)
//   HIGGSFIELD_BASE    = API base (default https://platform.higgsfield.ai)

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Pull an image URL out of whatever shape Higgsfield returns.
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

  const KEY = process.env.HIGGSFIELD_API_KEY;
  if (!KEY) return res.status(500).json({ error: 'HIGGSFIELD_API_KEY not set in Vercel env' });

  const BASE = (process.env.HIGGSFIELD_BASE || 'https://platform.higgsfield.ai').replace(/\/$/, '');
  const MODEL = (process.env.HIGGSFIELD_MODEL || 'nano-banana/text-to-image').replace(/^\//, '');

  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch { body = {}; } }
  body = body || {};
  const prompt = (body.prompt || '').toString().trim();
  const aspect_ratio = body.aspect_ratio || '3:4';
  const seed = body.seed;
  if (!prompt) return res.status(400).json({ error: 'prompt required' });

  const auth = { Authorization: 'Key ' + KEY, 'Content-Type': 'application/json' };
  const input = { prompt, aspect_ratio, ...(seed != null ? { seed } : {}) };

  try {
    // Submit
    const sub = await fetch(`${BASE}/${MODEL}`, { method: 'POST', headers: auth, body: JSON.stringify(input) });
    const subJson = await sub.json().catch(() => ({}));
    if (!sub.ok) return res.status(502).json({ error: `Higgsfield submit ${sub.status}`, detail: subJson });

    // Some models return the image inline on submit.
    let img = pickImage(subJson);
    if (img) return res.status(200).json({ image: img });

    const reqId = subJson.request_id || subJson.id;
    const statusUrl = subJson.status_url || (reqId ? `${BASE}/requests/${reqId}/status` : null);
    const responseUrl = subJson.response_url || (reqId ? `${BASE}/requests/${reqId}` : null);
    if (!statusUrl) return res.status(502).json({ error: 'no request id / status url from Higgsfield', detail: subJson });

    // Poll (up to ~90s)
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
  }
};
