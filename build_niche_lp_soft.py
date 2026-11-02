#!/usr/bin/env python3
"""Softer redesign of the niche landing pages. Reuses the copy from build_niche_lp.PAGES."""
import html, re
from build_niche_lp import PAGES, G1, G2, CAL, PHONE, PHONE_H, sms

IMG = {'dentists': 'dentists', 'tradies': 'tradies', 'clinics': 'clinics', 'summer': 'summer'}


def strip_hl(s):
    return re.sub(r'<span class="hl"[^>]*>(.*?)</span>', r'<span class="soft">\1</span>', s)


def page(c):
    e = html.escape
    SMS = sms("Hi Joel, I'd like a free Google preview for my business: ")
    pains = ''.join(f'<div class="pain"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in c['pains'])
    gets = ''.join(f'<li>{e(x)}</li>' for x in c['gets'])
    searches = ''.join(f'<span>{e(x)}</span>' for x in c['searches'])
    faqs = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in c['faqs'])
    ad = c['ad']
    img = IMG[c['slug']]
    return f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8">{G1}
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(c['title'])}</title><meta name="description" content="{e(c['desc'])}">
<link rel="canonical" href="https://www.margindigital.com.au/{c['slug']}">
<link rel="preload" as="image" href="/img/lp/{img}.webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap">
<script defer src="/_vercel/insights/script.js"></script>
<style>
:root{{--bg:#FAF7F2;--card:#FFFFFF;--sand:#F1EBE1;--ink:#1F2B2D;--ink2:#4A5759;--ink3:#7D8789;--line:#E7E0D5;--sage:#2F5D50;--sage-d:#244A40;--sage-l:#E4EDE8;--clay:#D9896A;color-scheme:light}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Plus Jakarta Sans",Helvetica,Arial,sans-serif;font-size:18px;line-height:1.7;font-weight:400;-webkit-font-smoothing:antialiased}}
em,i{{font-style:normal}}p{{margin:0}}a{{color:inherit}}img{{max-width:100%;display:block}}
h1,h2,h3{{margin:0;font-weight:700;letter-spacing:-.02em;text-wrap:balance}}
h1{{font-size:clamp(2.2rem,4.6vw,3.5rem);line-height:1.12}}h2{{font-size:clamp(1.6rem,3vw,2.3rem);line-height:1.2}}h3{{font-size:1.12rem;line-height:1.35;font-weight:600;letter-spacing:-.01em}}
.soft{{color:var(--sage)}}
.wrap{{max-width:1120px;margin:0 auto;padding:0 24px}}.narrow{{max-width:760px}}
section{{padding:clamp(56px,8vw,100px) 0}}
.eyebrow{{display:inline-flex;align-items:center;gap:8px;color:var(--sage);font-weight:600;font-size:.92rem;margin-bottom:18px}}
.eyebrow:before{{content:"";width:8px;height:8px;border-radius:50%;background:var(--clay)}}
.lead{{font-size:clamp(1.08rem,1.5vw,1.22rem);color:var(--ink2);margin-top:20px;max-width:52ch}}
.muted{{color:var(--ink2)}}
.top{{position:sticky;top:0;z-index:20;background:rgba(250,247,242,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}}
.top .wrap{{display:flex;align-items:center;justify-content:space-between;padding:14px 24px}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:700;text-decoration:none;font-size:1.05rem}}.brand i{{width:12px;height:12px;border-radius:50%;background:var(--sage);display:block}}
.top .ph{{text-decoration:none;font-weight:600;color:var(--sage);font-size:.98rem}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;font:inherit;font-weight:600;font-size:1.02rem;padding:15px 24px;border-radius:999px;text-decoration:none;background:var(--sage);color:#fff;border:1.5px solid var(--sage);transition:background .2s,transform .2s}}
.btn:hover{{background:var(--sage-d);transform:translateY(-1px)}}
.btn.ghost{{background:transparent;color:var(--ink);border-color:var(--line)}}.btn.ghost:hover{{background:var(--card);border-color:var(--ink3)}}
.btn.light{{background:#fff;color:var(--sage-d);border-color:#fff}}
.cta{{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}}
.note{{margin-top:16px;font-size:.92rem;color:var(--ink3)}}
.hero .wrap{{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}}@media(max-width:900px){{.hero .wrap{{grid-template-columns:1fr;gap:36px}}}}
.hero{{padding-top:clamp(36px,6vw,72px)}}
.photo{{position:relative}}
.photo img{{width:100%;aspect-ratio:4/3.4;object-fit:cover;border-radius:28px}}
.photo .chip{{position:absolute;left:-14px;bottom:28px;background:var(--card);border-radius:18px;padding:14px 18px;box-shadow:0 18px 40px rgba(31,43,45,.12);display:flex;gap:12px;align-items:center;max-width:290px}}
@media(max-width:900px){{.photo .chip{{left:14px}}}}
.photo .chip b{{display:block;font-size:.95rem;font-weight:600}}.photo .chip span{{font-size:.85rem;color:var(--ink2);line-height:1.4;display:block}}
.photo .chip .dot{{flex:0 0 38px;height:38px;border-radius:50%;background:var(--sage-l);display:grid;place-content:center;color:var(--sage);font-weight:700}}
.ticks{{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}}.ticks span{{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:7px 14px;font-size:.9rem;font-weight:500;color:var(--ink2)}}
.band{{background:var(--sand)}}
.pains{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}}@media(max-width:820px){{.pains{{grid-template-columns:1fr}}}}
.pain{{background:var(--card);border-radius:22px;padding:28px}}.pain h3{{margin-bottom:8px}}.pain p{{color:var(--ink2);font-size:1rem}}
.split{{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}}@media(max-width:860px){{.split{{grid-template-columns:1fr;gap:32px}}}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}}.chips span{{background:var(--sage-l);color:var(--sage-d);border-radius:999px;padding:7px 14px;font-size:.9rem;font-weight:500}}
.serp{{background:var(--card);border-radius:24px;padding:26px;font-family:Arial,Helvetica,sans-serif;box-shadow:0 24px 60px rgba(31,43,45,.10)}}
.serp .q{{background:#F1F3F4;border-radius:24px;padding:11px 16px;font-size:.95rem;color:#202124}}.serp .sp{{font-size:.78rem;font-weight:700;margin-top:18px;color:#202124}}.serp .u{{font-size:.82rem;margin-top:3px;color:#202124}}
.serp .h{{color:#1a0dab;font-size:1.1rem;margin-top:6px;line-height:1.35}}.serp .st{{color:#fbbc04;font-size:.85rem;margin-top:4px}}.serp .st span{{color:#4d5156}}.serp .d{{color:#4d5156;font-size:.9rem;margin-top:6px;line-height:1.55}}
.serp .c{{display:inline-block;margin-top:12px;background:#1a73e8;color:#fff;border-radius:20px;padding:8px 14px;font-weight:700;font-size:.88rem}}.serp .dim{{opacity:.38;border-top:1px solid #eee;margin-top:18px;padding-top:12px}}.serp small{{display:block;font-size:.78rem;color:#9aa3b2;margin-top:14px}}
.gets{{list-style:none;padding:0;margin:26px 0 0;display:grid;gap:14px}}.gets li{{display:flex;gap:14px;align-items:flex-start}}
.gets li:before{{content:"";flex:0 0 22px;height:22px;margin-top:4px;border-radius:50%;background:var(--sage-l) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%232F5D50' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat}}
.prices{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px}}@media(max-width:760px){{.prices{{grid-template-columns:1fr}}}}
.price{{background:var(--card);border-radius:24px;padding:30px;border:1px solid var(--line)}}.price.main{{background:var(--sage);color:#fff;border-color:var(--sage)}}
.price .amt{{font-size:2.6rem;font-weight:700;letter-spacing:-.03em;margin-top:10px;line-height:1}}.price .amt small{{font-size:.95rem;font-weight:500;color:var(--ink3);margin-left:6px;letter-spacing:0}}.price.main .amt small{{color:#CFE0D8}}
.price p{{margin-top:14px;font-size:1rem;color:var(--ink2)}}.price.main p{{color:#DCE8E2}}
.guar{{background:var(--card);border-radius:28px;padding:clamp(28px,5vw,48px);display:grid;grid-template-columns:auto 1fr;gap:32px;align-items:center;margin-top:20px;border:1px solid var(--line)}}@media(max-width:700px){{.guar{{grid-template-columns:1fr}}}}
.guar .big{{width:120px;height:120px;border-radius:50%;background:var(--sage-l);color:var(--sage);display:grid;place-content:center;font-size:1.9rem;font-weight:700;letter-spacing:-.03em}}
.guar p{{color:var(--ink2);margin-top:10px}}
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}}@media(max-width:820px){{.steps{{grid-template-columns:1fr}}}}
.step{{background:var(--card);border-radius:22px;padding:28px}}.step .n{{width:36px;height:36px;border-radius:50%;background:var(--sage);color:#fff;display:grid;place-content:center;font-weight:700;font-size:.95rem;margin-bottom:16px}}.step p{{color:var(--ink2);font-size:1rem;margin-top:8px}}
details{{background:var(--card);border-radius:18px;padding:20px 24px;margin-top:12px}}summary{{font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:16px}}summary::-webkit-details-marker{{display:none}}
summary:after{{content:"+";color:var(--sage);font-weight:700;font-size:1.3rem;line-height:1}}details[open] summary:after{{content:"−"}}details p{{margin-top:12px;color:var(--ink2);font-size:1rem}}
.final{{background:var(--sage);color:#fff;border-radius:32px;padding:clamp(36px,6vw,64px);text-align:center}}
.final h2{{color:#fff}}.final .soft{{color:#CFE7A9}}.final p{{color:#DCE8E2;margin:14px auto 0;max-width:52ch}}
.final .cta{{justify-content:center}}.final .btn.ghost{{color:#fff;border-color:rgba(255,255,255,.4)}}.final .btn.ghost:hover{{background:rgba(255,255,255,.08)}}
.cal{{background:#fff;border-radius:24px;overflow:hidden;margin-top:34px;min-height:660px}}
footer{{padding:36px 0 110px;text-align:center;color:var(--ink3);font-size:.9rem}}
.sticky{{display:none}}@media(max-width:860px){{.sticky{{display:flex;gap:10px;position:fixed;left:0;right:0;bottom:0;z-index:30;padding:10px 14px calc(10px + env(safe-area-inset-bottom,0px));background:rgba(250,247,242,.96);backdrop-filter:blur(10px);border-top:1px solid var(--line)}}.sticky .btn{{flex:1;padding:14px 10px}}.sticky .btn.ghost{{flex:0 0 auto;padding:14px 20px}}}}
</style></head><body>
<header class="top"><div class="wrap"><a class="brand" href="/"><i></i>Margin Digital</a><a class="ph" href="{PHONE_H}">{PHONE}</a></div></header>
<main>
<section class="hero"><div class="wrap">
  <div>
    <div class="eyebrow">{e(c['kick'])}</div>
    <h1>{strip_hl(c['h1'])}</h1>
    <p class="lead">{e(c['lead'])}</p>
    <div class="cta"><a class="btn" href="{SMS}">Get a free Google preview</a><a class="btn ghost" href="#book">Book a 15-minute call</a></div>
    <p class="note">Free, no obligation. Text me your business name and I will send a private preview within one business day.</p>
  </div>
  <div class="photo"><img src="/img/lp/{img}.webp" alt="" width="1200" height="1000" fetchpriority="high">
    <div class="chip"><div class="dot">✓</div><div><b>See it before you pay</b><span>A private preview of your ads at the top of Google.</span></div></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="narrow"><div class="eyebrow">Sound familiar?</div><h2>{e(c['pain_h']) if c['pain_h']!='Sound familiar?' else 'The problems we hear most often.'}</h2></div>
  <div class="pains">{pains}</div>
</div></section>

<section><div class="wrap split">
  <div>
    <div class="eyebrow">How it looks</div>
    <h2>{e(c['mock_h'])}</h2>
    <p class="lead">{e(c['mock_p'])}</p>
    <div class="chips">{searches}</div>
  </div>
  <div class="serp"><div class="q">{e(ad['q'])}</div><div class="sp">Sponsored</div><div class="u">yourbusiness.com.au</div><div class="h">{e(ad['h'])}</div><div class="st">★★★★★ <span>Your Google reviews</span></div><div class="d">{e(ad['d'])}</div><div class="c">{e(ad['cta'])}</div><div class="dim"><div class="sp">Sponsored</div><div class="h" style="font-size:1rem">A competitor's ad</div></div><small>Example shown with a placeholder business.</small></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="split" style="align-items:start">
    <div><div class="eyebrow">What you get</div><h2>Everything set up and looked after.</h2><p class="lead">Prices are on the page, there is no lock-in contract, and you deal with me directly.</p></div>
    <ul class="gets">{gets}</ul>
  </div>
  <div class="prices">
    <div class="price main"><h3>Google Ads management</h3><div class="amt">$799<small>per month, ex GST</small></div><p>Campaign built and managed for you, calls and bookings tracked, and a one-page monthly report. Ad spend is paid by you directly to Google. Month to month.</p></div>
    <div class="price"><h3>Website</h3><div class="amt">$2,500<small>once, ex GST</small></div><p>A fast, mobile-first site written for {e(c['who'])}, with calls and bookings wired up and your Google Business Profile set up alongside it. No monthly fee for the site.</p></div>
  </div>
  <div class="guar"><div class="big">100%</div><div><h2>Not happy at any point? Every dollar back.</h2><p>Say so and the fee you paid is refunded in full, and you keep everything that was built. Ad spend goes directly to Google and is not part of what I charge.</p></div></div>
</div></section>

<section><div class="wrap">
  <div class="narrow"><div class="eyebrow">How it works</div><h2>Three simple steps.</h2></div>
  <div class="steps">
    <div class="step"><div class="n">1</div><h3>Text me your business name</h3><p>That is all I need. I look at your website, your Google listing and your reviews.</p></div>
    <div class="step"><div class="n">2</div><h3>Get your free preview</h3><p>{e(c['step2'])}</p></div>
    <div class="step"><div class="n">3</div><h3>Live within a week</h3><p>If you like it, I build it. Calls and bookings are tracked from day one, and you can stop any month.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap narrow">
  <div class="eyebrow">Questions</div><h2>Good questions to ask.</h2>
  <div style="margin-top:24px">{faqs}</div>
</div></section>

<section id="book"><div class="wrap">
  <div class="final">
    <h2>{strip_hl(c['final_h'])}</h2>
    <p>Text me your business name for a free preview, give me a call, or pick a time that suits you below.</p>
    <div class="cta"><a class="btn light" href="{SMS}">Get a free Google preview</a><a class="btn ghost" href="{PHONE_H}">Call {PHONE}</a></div>
    <div class="cal"><div class="calendly-inline-widget" data-url="{CAL}?hide_gdpr_banner=1&primary_color=2f5d50" style="min-width:300px;height:660px"></div></div>
  </div>
</div></section>
</main>
<footer>Margin Digital · Sydney, working Australia-wide · <a href="{PHONE_H}">{PHONE}</a> · <a href="mailto:hello@margindigital.com.au">hello@margindigital.com.au</a></footer>
<div class="sticky"><a class="btn ghost" href="{PHONE_H}">Call</a><a class="btn" href="{SMS}">Free Google preview</a></div>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>
<script>window.addEventListener('message',function(e){{if(e.origin.indexOf('calendly.com')<0)return;if(e.data&&e.data.event==='calendly.event_scheduled'&&window.gtag){{gtag('event','conversion',{{'send_to':'AW-18536302130/KGlTCJmvlKkdELKM5oZF'}});}}}});</script>
{G2}
</body></html>'''


if __name__ == '__main__':
    for c in PAGES:
        open(f"public/{c['slug']}.html", 'w').write(page(c))
        print('built', c['slug'])
