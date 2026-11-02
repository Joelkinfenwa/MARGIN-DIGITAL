// Vercel serverless function: receives website leads.
// 1. Always records the lead in the "Margin Digital Website Leads" Google Form
//    (responses sheet + email notification to the form owner). No keys needed.
// 2. Also emails it via Resend once these env vars are set in Vercel:
//    RESEND_API_KEY, LEAD_TO_EMAIL, LEAD_FROM_EMAIL
const GFORM_URL = process.env.GFORM_URL ||
  'https://docs.google.com/forms/d/e/1FAIpQLSfaCO4tISpp8LG3uaHfeqhNn_5LFNYtMdYSnCgj2NOsaEpgnw/formResponse';
const F = { business: 'entry.996985704', mobile: 'entry.596368259', email: 'entry.760800595', interest: 'entry.1425429755', site: 'entry.2082358288', details: 'entry.975081997', page: 'entry.1326753538' };

const str = (v) => (typeof v === 'string' ? v.trim().slice(0, 500) : '');

async function toGoogleForm(b) {
  const details = [
    b.name && b.name !== 'Not given' ? `Name: ${b.name}` : '',
    b.goal ? `Wants: ${b.goal}` : '',
    b.message ? `Message: ${b.message}` : '',
    `Received: ${new Date().toLocaleString('en-AU', { timeZone: 'Australia/Sydney' })}`,
  ].filter(Boolean).join(' | ');
  const body = new URLSearchParams({
    [F.business]: b.business, [F.mobile]: b.mobile, [F.email]: b.email || '',
    [F.interest]: b.interest || 'Enquiry', [F.site]: b.site || '', [F.details]: details, [F.page]: b.page || '',
  });
  const r = await fetch(GFORM_URL, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body, redirect: 'manual' });
  if (r.status >= 400) throw new Error('Google Form status ' + r.status);
}

async function toResend(b) {
  const { RESEND_API_KEY, LEAD_TO_EMAIL, LEAD_FROM_EMAIL } = process.env;
  if (!RESEND_API_KEY || !LEAD_TO_EMAIL || !LEAD_FROM_EMAIL) return false;
  const esc = (s) => String(s || '').replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const rows = [['Name', b.name], ['Business', b.business], ['Mobile', b.mobile], ['Email', b.email], ['Interest', b.interest], ['Website', b.site], ['Wants', b.goal], ['Message', b.message], ['Page', b.page]]
    .map(([k, v]) => `<tr><td><b>${k}</b></td><td>${esc(v) || '—'}</td></tr>`).join('');
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: `Margin Digital <${LEAD_FROM_EMAIL}>`, to: [LEAD_TO_EMAIL], ...(b.email ? { reply_to: b.email } : {}),
      subject: `${b.interest || 'Enquiry'}: ${b.business}`,
      html: `<h2>New lead — Margin Digital</h2><table cellpadding="6" style="font-family:Arial,sans-serif;font-size:14px">${rows}</table>`,
    }),
  });
  if (!r.ok) throw new Error('Resend ' + r.status + ' ' + (await r.text()));
  return true;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
  const raw = req.body || {};
  const b = Object.fromEntries(['name', 'business', 'mobile', 'email', 'interest', 'site', 'goal', 'message', 'page'].map((k) => [k, str(raw[k])]));
  if (!b.business) return res.status(400).json({ error: 'Missing field: business' });
  if (b.mobile.replace(/\D/g, '').length < 8) return res.status(400).json({ error: 'Missing or invalid mobile' });
  if (b.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(b.email)) return res.status(400).json({ error: 'Invalid email' });

  const [g, r] = await Promise.allSettled([toGoogleForm(b), toResend(b)]);
  if (g.status === 'rejected') console.error('Google Form failed', g.reason);
  if (r.status === 'rejected') console.error('Resend failed', r.reason);
  if (g.status === 'fulfilled' || (r.status === 'fulfilled' && r.value)) return res.status(200).json({ ok: true });
  console.error('Lead NOT delivered', b);
  return res.status(502).json({ error: 'Delivery failed' });
}
