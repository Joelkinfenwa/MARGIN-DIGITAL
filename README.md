# Margin Digital — website

Static site (`public/`) plus one Vercel serverless function (`api/lead.js`) that emails each booking-form submission via Resend.

## Deploy
1. Push this folder to a GitHub repo.
2. In Vercel: New Project → import the repo. Framework preset: **Other**. Output directory: `public`.
3. Add environment variables: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL` (a sender on a domain verified in Resend).
4. Deploy. Test the form once; the email should arrive within seconds.

## Before launch
- Replace `0400 000 000` and `hello@margindigital.com.au` in `public/index.html` and `public/thanks.html`.
- Add the ABN to the footer.
- Add `public/privacy.html` and `public/terms.html` (footer links point to them).
