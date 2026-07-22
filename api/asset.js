// Internal asset relay for BAEZ tooling.
//
// Fetches a generated Takeover asset from the Higgsfield CDN server-side and
// returns it base64-encoded, so build tooling that cannot reach the CDN
// directly (sandboxed CI, PDF assembly) can still retrieve our own artwork.
// Locked to OUR user path on the CDN — this cannot fetch arbitrary URLs.
//
// GET /api/asset?file=hf_..._<jobid>.png[&start=N&len=M]
//   -> { size, start, len, b64 }   (chunk of the binary, base64)

const CDN = 'https://d8j0ntlcm91z4.cloudfront.net/user_367Twnt1CjgstYSJuY3u52mI2QL/';
const NAME_RE = /^hf_[A-Za-z0-9_-]+\.(png|webp|jpg)$/;
const MAX_CHUNK = 3_000_000; // bytes of binary per response (~4MB base64)

module.exports = async (req, res) => {
  if (req.method !== 'GET') return res.status(405).json({ error: 'GET only' });
  const q = req.query || {};
  const file = (q.file || '').toString();
  if (!NAME_RE.test(file)) return res.status(400).json({ error: 'bad file name' });

  const start = Math.max(0, parseInt(q.start || '0', 10) || 0);
  const len = Math.min(MAX_CHUNK, Math.max(1, parseInt(q.len || String(MAX_CHUNK), 10) || MAX_CHUNK));

  try {
    const r = await fetch(CDN + file);
    if (!r.ok) return res.status(502).json({ error: 'cdn ' + r.status });
    const buf = Buffer.from(await r.arrayBuffer());
    const slice = buf.subarray(start, start + len);
    return res.status(200).json({
      size: buf.length,
      start,
      len: slice.length,
      b64: slice.toString('base64'),
    });
  } catch (e) {
    return res.status(500).json({ error: 'relay error: ' + (e && e.message || e) });
  }
};
