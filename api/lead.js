// Vercel serverless function: receives the booking form and emails it via Resend.
// Environment variables (set in Vercel → Project → Settings → Environment Variables):
//   RESEND_API_KEY   — from resend.com
//   LEAD_TO_EMAIL    — where leads should land, e.g. joel@example.com
//   LEAD_FROM_EMAIL  — a verified sender on your Resend domain, e.g. leads@margindigital.com.au
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const b = req.body || {};
  const required = ['name', 'business', 'mobile', 'email'];
  for (const k of required) {
    if (!b[k] || typeof b[k] !== 'string' || b[k].length > 500) return res.status(400).json({ error: `Missing or invalid field: ${k}` });
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(b.email)) return res.status(400).json({ error: 'Invalid email' });
  const { RESEND_API_KEY, LEAD_TO_EMAIL, LEAD_FROM_EMAIL } = process.env;
  if (!RESEND_API_KEY || !LEAD_TO_EMAIL || !LEAD_FROM_EMAIL) {
    console.error('Lead received but email env vars are not set', b);
    return res.status(500).json({ error: 'Email not configured' });
  }
  const esc = (s) => String(s || '').replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const html = `
    <h2>New enquiry — Margin Digital</h2>
    <table cellpadding="6" style="font-family:Arial,sans-serif;font-size:14px">
      <tr><td><b>Name</b></td><td>${esc(b.name)}</td></tr>
      <tr><td><b>Business</b></td><td>${esc(b.business)}</td></tr>
      <tr><td><b>Mobile</b></td><td>${esc(b.mobile)}</td></tr>
      <tr><td><b>Email</b></td><td>${esc(b.email)}</td></tr>
      <tr><td><b>Interest</b></td><td>${esc(b.interest) || '—'}</td></tr>
      <tr><td><b>Website</b></td><td>${esc(b.site) || '—'}</td></tr>
      <tr><td><b>Wants more of</b></td><td>${esc(b.goal) || '—'}</td></tr>
      <tr><td><b>Page</b></td><td>${esc(b.page)}</td></tr>
      <tr><td><b>Received</b></td><td>${new Date().toLocaleString('en-AU', { timeZone: 'Australia/Sydney' })}</td></tr>
    </table>`;
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: `Margin Digital <${LEAD_FROM_EMAIL}>`,
      to: [LEAD_TO_EMAIL],
      reply_to: b.email,
      subject: `${b.interest || 'Enquiry'}: ${b.business}`,
      html,
    }),
  });
  if (!r.ok) {
    console.error('Resend error', r.status, await r.text());
    return res.status(502).json({ error: 'Email send failed' });
  }
  return res.status(200).json({ ok: true });
}
