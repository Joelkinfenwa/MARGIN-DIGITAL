#!/usr/bin/env python3
"""Builds single-goal niche landing pages for Google Ads and outreach.
Every call to action is a phone call, a text or a Calendly booking (all working without a form backend)."""
import html

SCRATCH = '/tmp/claude-0/-home-claude/582cdbaf-aeb3-50fd-b31c-3c888845266a/scratchpad/'
G1 = open(SCRATCH + 'g1.html').read()
G2 = open(SCRATCH + 'g2.html').read()
CAL = 'https://calendly.com/hello-margindigital/30min'
PHONE_H = 'tel:+61449022604'
PHONE = '0449 022 604'


def sms(body):
    from urllib.parse import quote
    return 'sms:+61449022604?&body=' + quote(body)


def page(c):
    e = html.escape
    SMS = sms(c.get('sms', "Hi Joel, I'd like a free Google preview for my business: "))
    pains = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in c['pains'])
    gets = ''.join(f'<li>{e(x)}</li>' for x in c['gets'])
    searches = ''.join(f'<span>{e(x)}</span>' for x in c['searches'])
    faqs = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in c['faqs'])
    ad = c['ad']
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8">{G1}
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(c['title'])}</title><meta name="description" content="{e(c['desc'])}">
<link rel="canonical" href="https://www.margindigital.com.au/{c['slug']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@500;600;700;800;900&display=swap">
<script defer src="/_vercel/insights/script.js"></script>
<style>
:root{{--ink:#0B1E3F;--ink2:#3E4C66;--ink3:#7A8699;--line:#E1E6EE;--bg:#fff;--surface:#F4F6F9;--mark:#D4F23A;--ok:#1C9B5E;--acc:{c['accent']};color-scheme:light}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:Figtree,Helvetica,Arial,sans-serif;font-size:18px;line-height:1.55;font-weight:500;-webkit-font-smoothing:antialiased}}
em,i{{font-style:normal}}p{{margin:0}}a{{color:inherit}}h1,h2,h3{{margin:0;line-height:1.04;letter-spacing:-.03em;font-weight:900;text-wrap:balance}}
h1{{font-size:clamp(2.5rem,6.4vw,5rem)}}h2{{font-size:clamp(1.8rem,4vw,3rem)}}h3{{font-size:1.2rem;font-weight:800;letter-spacing:-.01em}}
.wrap{{max-width:1100px;margin:0 auto;padding:0 20px}}section{{padding:clamp(56px,8vw,96px) 0}}
.annc{{background:var(--mark);font-weight:800;text-align:center;font-size:.95rem;padding:10px 16px}}.annc a{{text-underline-offset:3px}}
.top{{border-bottom:1px solid var(--line);background:#fff;position:sticky;top:0;z-index:20}}.top .wrap{{display:flex;align-items:center;justify-content:space-between;padding:12px 20px}}
.brand{{display:flex;align-items:center;gap:9px;font-weight:900;font-size:1.1rem;text-decoration:none;letter-spacing:-.02em}}.brand i{{width:13px;height:13px;background:#2449E6;border-radius:3px;transform:rotate(45deg);display:block}}
.top a.ph{{font-weight:800;text-decoration:none;color:#2449E6}}
.kick{{display:inline-block;background:var(--ink);color:#fff;font-weight:800;font-size:.85rem;padding:7px 14px;border-radius:999px;margin-bottom:18px;letter-spacing:.01em}}
.hl{{background:linear-gradient(transparent 58%,var(--mark) 58%,var(--mark) 92%,transparent 92%);padding:0 .05em}}
.hero{{padding-top:clamp(32px,5vw,60px)}}.hero .wrap{{display:grid;grid-template-columns:1.15fr .85fr;gap:44px;align-items:center}}@media(max-width:900px){{.hero .wrap{{grid-template-columns:1fr}}}}
.lead{{font-size:clamp(1.15rem,1.8vw,1.4rem);color:var(--ink2);margin-top:20px;max-width:54ch}}
.ticks{{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:20px;font-weight:700;font-size:1rem}}.ticks span:before{{content:"✓";color:var(--ok);margin-right:7px;font-weight:900}}
.card{{background:var(--ink);color:#fff;border-radius:22px;padding:28px;box-shadow:0 30px 70px rgba(11,30,63,.28);position:relative}}
.card .badge{{position:absolute;top:-14px;left:24px;background:var(--mark);color:var(--ink);font-weight:900;font-size:.8rem;padding:6px 12px;border-radius:999px}}
.card h2{{font-size:clamp(1.5rem,2.4vw,2rem);color:#fff}}.card p{{color:#C9D3E6;margin-top:10px;font-size:1rem}}
.btn{{display:flex;align-items:center;justify-content:center;gap:10px;font:inherit;font-weight:900;font-size:1.1rem;padding:18px 22px;border-radius:14px;text-decoration:none;background:var(--mark);color:var(--ink);transition:transform .15s;text-align:center}}.btn:hover{{transform:translateY(-2px)}}
.btn.dark{{background:var(--ink);color:#fff}}.btn.o{{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.35)}}.btn.ol{{background:#fff;color:var(--ink);border:2px solid var(--ink)}}
.stack{{display:grid;gap:10px;margin-top:20px}}.card small{{display:block;margin-top:12px;color:#93A3BF;font-size:.85rem;text-align:center}}
.alt{{background:var(--surface)}}
.pains{{list-style:none;padding:0;margin:30px 0 0;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}@media(max-width:820px){{.pains{{grid-template-columns:1fr}}}}
.pains li{{background:#fff;border:2px solid var(--ink);border-radius:18px;padding:22px;box-shadow:7px 7px 0 var(--mark)}}.pains b{{display:block;font-size:1.15rem;font-weight:900}}.pains span{{display:block;margin-top:8px;color:var(--ink2);font-size:1rem}}
.mock{{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:center}}@media(max-width:820px){{.mock{{grid-template-columns:1fr}}}}
.serp{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;font-family:Arial,Helvetica,sans-serif;box-shadow:0 20px 50px rgba(11,30,63,.12)}}
.serp .q{{background:#F1F3F4;border-radius:24px;padding:11px 16px;font-size:.95rem}}.serp .sp{{font-size:.78rem;font-weight:700;margin-top:16px}}.serp .u{{font-size:.82rem;margin-top:3px}}
.serp .h{{color:#1a0dab;font-size:1.12rem;margin-top:6px;line-height:1.3}}.serp .st{{color:#fbbc04;font-size:.85rem;margin-top:4px}}.serp .st span{{color:#4d5156}}.serp .d{{color:#4d5156;font-size:.88rem;margin-top:5px;line-height:1.5}}
.serp .c{{display:inline-block;margin-top:10px;background:#1a73e8;color:#fff;border-radius:20px;padding:8px 14px;font-weight:700;font-size:.88rem}}.serp .dim{{opacity:.4;border-top:1px solid #eee;margin-top:16px;padding-top:12px}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}}.chips span{{background:#fff;border:1.5px solid var(--line);border-radius:999px;padding:7px 13px;font-weight:700;font-size:.92rem}}
.gets{{list-style:none;padding:0;margin:20px 0 0;display:grid;gap:12px}}.gets li{{display:flex;gap:12px;font-weight:600}}.gets li:before{{content:"✓";flex:0 0 28px;height:28px;border-radius:50%;background:var(--mark);display:grid;place-content:center;font-weight:900;font-size:.9rem}}
.price{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:28px}}@media(max-width:760px){{.price{{grid-template-columns:1fr}}}}
.pr{{border:2px solid var(--ink);border-radius:18px;padding:24px;background:#fff}}.pr.hot{{background:var(--ink);color:#fff}}.pr .a{{font-size:2.6rem;font-weight:900;letter-spacing:-.04em;line-height:1;margin-top:8px}}.pr .a small{{font-size:.9rem;font-weight:700;color:var(--ink3);letter-spacing:0;margin-left:6px}}.pr.hot .a small{{color:#C9D3E6}}.pr p{{margin-top:10px;font-size:1rem;color:var(--ink2)}}.pr.hot p{{color:#C9D3E6}}
.guar{{background:var(--mark)}}.guar .wrap{{display:grid;grid-template-columns:auto 1fr;gap:30px;align-items:center}}@media(max-width:700px){{.guar .wrap{{grid-template-columns:1fr}}}}.guar b{{font-size:clamp(4rem,10vw,7rem);font-weight:900;letter-spacing:-.05em;line-height:.9}}.guar h2{{font-size:clamp(1.6rem,3.4vw,2.4rem)}}.guar p{{margin-top:10px;font-size:1.08rem}}
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}}@media(max-width:820px){{.steps{{grid-template-columns:1fr}}}}.steps div{{border-top:4px solid var(--ink);padding-top:16px}}.steps b{{font-size:2.6rem;font-weight:900;line-height:1}}.steps p{{color:var(--ink2);margin-top:8px;font-size:1rem}}
details{{border-bottom:1px solid var(--line);padding:18px 0}}summary{{font-weight:800;cursor:pointer;font-size:1.08rem;list-style:none}}summary::-webkit-details-marker{{display:none}}summary:after{{content:"+";float:right;font-weight:900}}details[open] summary:after{{content:"–"}}details p{{margin-top:10px;color:var(--ink2)}}
.final{{background:var(--ink);color:#fff}}.final h2{{color:#fff;text-align:center}}.final .sub{{color:#C9D3E6;text-align:center;max-width:56ch;margin:14px auto 0;font-size:1.1rem}}
.final .row{{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:24px}}.final .row .btn{{min-width:250px}}.final .hl{{background:none;color:var(--mark)}}
.cal{{background:#fff;border-radius:18px;margin-top:30px;overflow:hidden;min-height:660px}}
footer{{padding:24px 0 100px;color:var(--ink3);font-size:.88rem;text-align:center}}
.sticky{{display:none}}@media(max-width:860px){{.sticky{{display:flex;gap:10px;position:fixed;left:0;right:0;bottom:0;z-index:30;padding:10px 14px calc(10px + env(safe-area-inset-bottom,0px));background:rgba(255,255,255,.97);border-top:1px solid var(--line)}}.sticky .btn{{flex:1;padding:15px 10px;font-size:1rem}}.sticky .btn.ol{{flex:0 0 auto;padding:15px 18px}}}}
</style></head><body>
<div class="annc">{e(c['annc'])} <a href="{SMS}">Text me for yours →</a></div>
<header class="top"><div class="wrap"><a class="brand" href="/"><i></i>Margin Digital</a><a class="ph" href="{PHONE_H}">{PHONE}</a></div></header>
<main>
<section class="hero"><div class="wrap">
  <div>
    <span class="kick">{e(c['kick'])}</span>
    <h1>{c['h1']}</h1>
    <p class="lead">{e(c['lead'])}</p>
    <div class="ticks"><span>Prices on this page</span><span>No lock-in contract</span><span>You deal with me directly</span><span>100% money back</span></div>
  </div>
  <div class="card" id="preview">
    <div class="badge">FREE · NO OBLIGATION</div>
    <h2>{e(c['card_h'])}</h2>
    <p>{e(c['card_p'])}</p>
    <div class="stack">
      <a class="btn" href="{SMS}">Text me for my free preview →</a>
      <a class="btn o" href="#book">Or book a 15-minute call</a>
    </div>
    <small>Joel · {PHONE} · Sydney, working Australia-wide</small>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>{e(c['pain_h'])}</h2>
  <ul class="pains">{pains}</ul>
</div></section>

<section><div class="wrap mock">
  <div>
    <h2>{e(c['mock_h'])}</h2>
    <p class="lead" style="font-size:1.1rem">{e(c['mock_p'])}</p>
    <div class="chips">{searches}</div>
  </div>
  <div class="serp"><div class="q">{e(ad['q'])}</div><div class="sp">Sponsored</div><div class="u">yourbusiness.com.au</div><div class="h">{e(ad['h'])}</div><div class="st">★★★★★ <span>Your Google reviews</span></div><div class="d">{e(ad['d'])}</div><div class="c">{e(ad['cta'])}</div><div class="dim"><div class="sp">Sponsored</div><div class="h" style="font-size:1rem">A competitor's ad</div></div><p style="font-size:.78rem;color:#9aa3b2;margin-top:12px">Example with a placeholder business.</p></div>
</div></section>

<section class="alt"><div class="wrap">
  <h2>What you get.</h2>
  <ul class="gets">{gets}</ul>
  <div class="price">
    <div class="pr hot"><h3>Google Ads management</h3><div class="a">$799<small>/month ex GST</small></div><p>Campaign built and managed for you, calls and bookings tracked, a one-page monthly report. Ad spend is paid by you directly to Google. Month to month, no lock-in.</p></div>
    <div class="pr"><h3>Website</h3><div class="a">$2,500<small>once, ex GST</small></div><p>A fast, mobile-first site written for {e(c['who'])}, with calls and bookings wired up and your Google Business Profile set up alongside it. No monthly fee for the site.</p></div>
  </div>
</div></section>

<section class="guar"><div class="wrap"><b>100%</b><div><h2>Not happy at any point? Every dollar back.</h2><p>No fine print. Say so and the fee you paid is refunded in full, and you keep everything that was built. Ad spend goes directly to Google and is not part of what I charge.</p></div></div></section>

<section><div class="wrap">
  <h2>How it works.</h2>
  <div class="steps">
    <div><b>01</b><h3>Text me your business name</h3><p>That is all I need to start. I look at your website, your Google listing and your reviews.</p></div>
    <div><b>02</b><h3>Get your free preview</h3><p>{e(c['step2'])}</p></div>
    <div><b>03</b><h3>Live within a week</h3><p>If you like it, I build it. Calls and bookings are tracked from day one. Stop any month.</p></div>
  </div>
</div></section>

<section class="alt"><div class="wrap" style="max-width:820px">
  <h2 style="margin-bottom:12px">Questions.</h2>
  {faqs}
</div></section>

<section class="final" id="book"><div class="wrap">
  <h2>{c['final_h']}</h2>
  <p class="sub">Text me your business name for a free preview, call me, or pick a time below.</p>
  <div class="row"><a class="btn" href="{SMS}">Text me for my free preview →</a><a class="btn ol" href="{PHONE_H}">Call {PHONE}</a></div>
  <div class="cal"><div class="calendly-inline-widget" data-url="{CAL}?hide_gdpr_banner=1&primary_color=0b1e3f" style="min-width:300px;height:660px"></div></div>
</div></section>
</main>
<footer>Margin Digital · Sydney, Australia · <a href="{PHONE_H}">{PHONE}</a> · <a href="mailto:hello@margindigital.com.au">hello@margindigital.com.au</a> · <a href="/privacy">Privacy</a></footer>
<div class="sticky"><a class="btn ol" href="{PHONE_H}">Call</a><a class="btn" href="{SMS}">Free preview</a></div>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>
<script>window.addEventListener('message',function(e){{if(e.origin.indexOf('calendly.com')<0)return;if(e.data&&e.data.event==='calendly.event_scheduled'&&window.gtag){{gtag('event','conversion',{{'send_to':'AW-18536302130/KGlTCJmvlKkdELKM5oZF'}});}}}});</script>
{G2}
</body></html>'''


PAGES = [
dict(slug='dentists', accent='#2449E6', who='dental practices',
 title='Google Ads and Websites for Dental Practices | Margin Digital',
 desc='Google Ads and websites for dental practices. See your practice at the top of Google for implant, Invisalign and new-patient searches before you spend a cent. $799/mo, no lock-in, 100% money back.',
 annc='Free: see your practice at the top of Google, built before you pay a cent.',
 kick='For dental practices',
 h1='More new patients in the chair. <span class="hl">Fewer empty slots.</span>',
 lead='When someone nearby searches for implants, Invisalign or a new dentist, your practice should be the first one they see and book. I run your Google Ads and build your website, and if you are not happy at any point, you get every dollar back.',
 card_h='See your practice at the top of Google. Before you spend a cent.',
 card_p='I build a private preview of your Google ads, written from your own website and reviews, so you can judge the work before deciding anything.',
 pain_h='Sound familiar?',
 pains=[('Gaps in the book','Hygiene and new-patient slots sitting empty while the practice down the road is booked out.'),
        ('Agencies that report clicks','Monthly reports full of impressions and clicks, and no idea how many patients actually booked.'),
        ('Ad rules nobody explained','Testimonials, before-and-after claims and treatment wording all have AHPRA rules. Most generalist agencies do not know them.')],
 mock_h='Show up for the searches that fill the book.',
 mock_p='Campaigns aimed at the treatments you want more of, in the suburbs you serve, with every call and online booking tracked back to the search that caused it.',
 searches=['dental implants near me','invisalign [your suburb]','emergency dentist','new patient check up','dentist [your suburb]','teeth whitening'],
 ad=dict(q='dental implants near me', h='Dental Implants | Book a Consultation | Your Practice Name', d='Experienced local dentists. Clear pricing, payment plans available, and a friendly team. Book online in under a minute.', cta='Book online'),
 gets=['Google Ads campaign built around the treatments you want more of','Ad copy written with AHPRA advertising rules in mind, approved by you before it runs','Every call and online booking tracked, so you see cost per new patient','A one-page monthly report and a call to walk through it','All accounts in your practice\'s name, so you keep everything'],
 step2='A private page showing your ads at the top of Google, the treatments they target and the suburbs they cover. Yours to keep either way.',
 faqs=[('Do you understand AHPRA advertising rules?','Yes. Ads and pages are written to avoid testimonials, misleading claims and outcome promises, and nothing goes live until you have approved the wording.'),
       ('How much should we spend on ads?','That is your call. The video audit includes a suggested starting budget for your area, and you can raise, lower or pause it at any time.'),
       ('Do we have to sign a contract?','No. Management is month to month. The website is a one-off fee.'),
       ('Will it work with our booking system?','Ads can send people straight to your existing online booking page, and those bookings are tracked as results.'),
       ('Who actually does the work?','I do. You have my mobile, and there is no account manager in between.')],
 final_h='Ready to see your practice <span class="hl">at the top of Google?</span>'),
dict(slug='tradies', accent='#2449E6', who='tradies',
 title='Google Ads and Websites for Tradies | Your Own Leads, Not Shared Ones | Margin Digital',
 desc='Google Ads and websites for plumbers, electricians, builders and trades. Your own leads, not shared with three competitors. $799/mo, no lock-in, 100% money back.',
 annc='Free: see your business at the top of Google, built before you pay a cent.',
 kick='For plumbers, electricians, builders and trades',
 h1='Your own leads. <span class="hl">Not shared with three other tradies.</span>',
 lead='When someone in your area searches for what you do, they should see your business first and call your phone, not fill in a form that goes to four competitors. I build the website and run the Google Ads, and if it does not bring you work, you get every dollar back.',
 card_h='See your business at the top of Google. Before you spend a cent.',
 card_p='I build a private preview of your Google ads, written from your own website and reviews, so you can judge it before you decide anything.',
 pain_h='Sound familiar?',
 pains=[('Paying for shared leads','Paying for a lead, then racing three other tradies to call back first, and losing on price.'),
        ('Flat out, then dead quiet','Too busy one month and chasing work the next, with nothing steady bringing in calls.'),
        ('Burnt by marketing before','Contracts you could not get out of, and reports nobody could explain.')],
 mock_h='The calls come to you. Only you.',
 mock_p='Ads that show your name, your stars and your phone number at the top of Google, in the suburbs you actually work, during the hours you can take the call.',
 searches=['plumber near me','emergency electrician','blocked drain [suburb]','builder [suburb]','hot water repair','roof repairs near me'],
 ad=dict(q='plumber near me', h='Local Plumber | On Our Way Today | Your Business Name', d='Licensed, local and five-star rated. Burst pipes, blocked drains and hot water. Upfront price before we start.', cta='📞 Call now'),
 gets=['Google Ads in your suburbs, during your hours, sending calls straight to your phone','Every call tracked, so you know what each job cost to win','A website built to get the phone ringing, if you need one','A one-page monthly report you can read in two minutes','Everything in your name: the ad account, the website, the data'],
 step2='A private page showing your ads at the top of Google, the searches they target and the hours they run. Yours to keep either way.',
 faqs=[('How is this different from hipages or Oneflare?','Those platforms sell the same lead to several businesses. With your own ads, the person searching calls you and only you, and you control the budget.'),
       ('How much do I need to spend on ads?','Your call. The video audit suggests a starting budget for your area, and you can change or pause it any time.'),
       ('Is there a lock-in contract?','No. Month to month. Stop whenever you like.'),
       ('I am already flat out. Why now?','Because the quiet months are when it matters, and a campaign takes a few weeks to tune. Set it up while you are busy and it is ready when you are not.'),
       ('Who does the work?','I do. You get my mobile, not an account manager.')],
 final_h='Ready for calls that <span class="hl">come to you first?</span>'),
dict(slug='clinics', accent='#2449E6', who='health clinics',
 title='Google Ads and Websites for Physio, Chiro and Allied Health Clinics | Margin Digital',
 desc='Google Ads and websites for physiotherapy, chiropractic and allied health clinics. More new patients booking online. $799/mo, no lock-in, 100% money back.',
 annc='Free: see your clinic at the top of Google, built before you pay a cent.',
 kick='For physio, chiro and allied health clinics',
 h1='More new patients <span class="hl">booking online.</span>',
 lead='When someone nearby searches for a physio, chiro or podiatrist, your clinic should be the one they book. I run your Google Ads and build your website, wired straight into your online bookings, and if you are not happy at any point you get every dollar back.',
 card_h='See your clinic at the top of Google. Before you spend a cent.',
 card_p='I build a private preview of your Google ads, written from your own website and reviews, so you can judge the work before deciding anything.',
 pain_h='Sound familiar?',
 pains=[('Practitioners with gaps','Practitioners on the books and appointment slots going unfilled during the week.'),
        ('Relying on referrals','Most new patients still come from GPs and word of mouth, which is hard to grow on purpose.'),
        ('Health ad rules','Testimonials and treatment claims have AHPRA rules, and generalist agencies often get them wrong.')],
 mock_h='Be found by the patients already looking.',
 mock_p='Ads that send people straight to your online booking page, in your suburbs, with every booking tracked back to the search that brought it in.',
 searches=['physio near me','sports physio [suburb]','chiropractor near me','podiatrist [suburb]','back pain treatment','remedial massage near me'],
 ad=dict(q='physio near me', h='Physiotherapy | Book Online Today | Your Clinic Name', d='Experienced local physiotherapists. Sports injuries, back and neck pain, rehab. Book in under a minute.', cta='Book online'),
 gets=['Google Ads aimed at the services and practitioners with the most availability','Ads sent straight to your existing online booking page','Ad wording written with AHPRA rules in mind, approved by you first','Every booking and call tracked, so you see cost per new patient','A one-page monthly report and a call to go through it'],
 step2='A private page showing your clinic at the top of Google, the searches it targets and the suburbs it covers. Yours to keep either way.',
 faqs=[('Does this work with Cliniko, Nookal or our booking system?','Ads can send people straight to your existing online booking page, and completed bookings can be tracked as results.'),
       ('Do you know the AHPRA advertising rules?','Yes. No testimonials, no misleading claims, and nothing goes live until you have approved the wording.'),
       ('How much should we spend?','Your call. The video audit includes a suggested starting budget, and you can change it any time.'),
       ('Is there a contract?','No. Month to month.'),
       ('Who does the work?','I do, directly. You have my mobile.')],
 final_h='Ready to fill the <span class="hl">empty appointment slots?</span>'),
dict(slug='summer', accent='#2449E6', who='seasonal service businesses',
 title='Get Your Business Ready for Summer | Google Ads and Websites | Margin Digital',
 desc='Air conditioning, pools, pest control, lawns and Christmas lights: be the first business people call when summer demand hits. Free Google preview. $799/mo, no lock-in, 100% money back.',
 annc='Summer demand starts now. See your business at the top of Google for free.',
 kick='For air con, pool, pest control, lawn and Christmas light businesses',
 h1='Summer is your busiest season. <span class="hl">Be the first number they call.</span>',
 lead='The first hot week, the first wasp nest, the first "lawn guy near me": the business at the top of Google gets the call. Campaigns take a couple of weeks to tune, so the time to set it up is before the rush, not during it.',
 card_h='See your business at the top of Google. Before summer starts.',
 card_p='I build a private preview of your Google ads for the summer rush, written from your own website and reviews. Free, and yours to keep.',
 pain_h='Every summer it is the same.',
 pains=[('The phone rings for someone else','Demand spikes, and the businesses at the top of Google take the calls.'),
        ('Too late to set up','By the time it is busy, there is no time to build a website or a campaign.'),
        ('Then it goes quiet','When the season ends there is nothing in place to keep work coming in.')],
 mock_h='Ready before the first hot week.',
 mock_p='Ads that switch on with demand, focus on the suburbs you service, and can be scaled up on the hottest days and paused when you are fully booked.',
 searches=['air conditioning installation','pool cleaning near me','pest control [suburb]','lawn mowing near me','christmas light installers','split system install'],
 ad=dict(q='air conditioning installation', h='Split System Installation | Fast Install This Week | Your Business', d='Licensed local installers. Supply and install, upfront quotes, five-star rated. Beat the heat, book before the rush.', cta='📞 Call now'),
 gets=['A summer campaign ready before demand peaks','Budget you can turn up on hot days and pause when you are booked out','Every call tracked back to the search that caused it','A website that gets the phone ringing, if you need one','Month to month, so you can stop when the season ends'],
 step2='A private page showing your business at the top of Google for summer searches in your area. Yours to keep either way.',
 faqs=[('Can I just run it for the summer?','Yes. Management is month to month, so you can run it through the season and stop.'),
       ('How fast can it be live?','Within a week of your go-ahead, which is why it is worth starting now.'),
       ('How much should I spend on ads?','Your call. The video audit suggests a budget for your area, and you can turn it up or down daily.'),
       ('Who does the work?','I do. You have my mobile.')],
 final_h='Get set up <span class="hl">before the rush.</span>'),
]

if __name__ == '__main__':
    for c in PAGES:
        open(f"public/{c['slug']}.html", 'w').write(page(c))
        print('built', c['slug'])
