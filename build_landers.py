#!/usr/bin/env python3
"""Generates the three ad landing pages: public/start.html, public/website.html, public/ads.html."""
import html, pathlib

CAL = "https://calendly.com/hello-margindigital/30min"
TEL = "tel:+61449022604"
PHONE = "0449 022 604"

HEAD = """<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<!-- Google tag (gtag.js), loaded after page load to keep the page fast -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-18536302130');
  (function(){var done=false;function load(){if(done)return;done=true;var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=AW-18536302130';document.head.appendChild(s);}
  window.addEventListener('load',function(){setTimeout(load,1500);});
  ['pointerdown','touchstart','keydown','scroll'].forEach(function(ev){window.addEventListener(ev,load,{once:true,passive:true});});})();
</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@500;600;700;800;900&display=swap">
<style>
:root{--bg:#fff;--surface:#F3F6FA;--surface-2:#E7ECF4;--ink:#0B1E3F;--ink-2:#3E4C66;--ink-3:#7A8699;--line:#D5DCE8;--accent:#2449E6;--mark:#D4F23A;--ok:#1C9B5E;--font:"Figtree","Helvetica Neue",Arial,sans-serif;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);font-size:18px;line-height:1.5;font-weight:500;-webkit-font-smoothing:antialiased}
em,i{font-style:normal}a{color:inherit}
h1,h2,h3{margin:0;line-height:1.05;letter-spacing:-.02em;font-weight:800;text-wrap:balance}
h1{font-size:clamp(2.4rem,5.6vw,4.2rem);font-weight:900;letter-spacing:-.03em}h2{font-size:clamp(1.75rem,3.6vw,2.6rem)}h3{font-size:1.2rem}
p{margin:0}
.wrap{max-width:1040px;margin:0 auto;padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font:inherit;font-weight:800;font-size:1.1rem;padding:18px 30px;border-radius:10px;text-decoration:none;background:var(--accent);color:#fff;border:0;cursor:pointer;box-shadow:0 8px 24px rgba(36,73,230,.25)}
.btn:hover{background:#1B3BC4}
.btn.ghost{background:#fff;color:var(--ink);border:2px solid var(--line);box-shadow:none}.btn.ghost:hover{border-color:var(--ink)}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
section{padding-block:clamp(52px,7vw,92px)}
.kicker{font-weight:700;color:var(--accent);margin-bottom:14px}
.lead{font-size:clamp(1.12rem,1.7vw,1.35rem);color:var(--ink-2);max-width:58ch}
.top{border-bottom:1px solid var(--line);position:sticky;top:env(safe-area-inset-top,0px);z-index:10;background:rgba(255,255,255,.94);backdrop-filter:blur(8px)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;padding-block:14px;gap:16px}
.brand{font-weight:900;font-size:1.25rem;letter-spacing:-.03em;text-decoration:none;display:flex;align-items:center;gap:9px}.brand .mk{width:14px;height:14px;background:var(--accent);border-radius:3px;transform:rotate(45deg)}
.top .call{font-weight:700;text-decoration:none;color:var(--ink-2);white-space:nowrap}
.top .btn{padding:11px 18px;font-size:.98rem}
@media (max-width:640px){.top .btn{display:none}.top .call{color:var(--accent)}}
.hero{padding-block:clamp(40px,6vw,80px) clamp(32px,5vw,56px)}
.hero .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:44px;align-items:start}
@media (max-width:900px){.hero .wrap{grid-template-columns:1fr;gap:28px}}
.pill{display:inline-flex;align-items:center;gap:8px;background:var(--mark);color:var(--ink);font-weight:800;font-size:.9rem;padding:8px 14px;border-radius:999px;margin-bottom:22px}
.pill i{width:8px;height:8px;border-radius:50%;background:var(--ink)}
.hero .lead{margin-top:20px}
.cta{margin-top:26px;display:flex;flex-direction:column;gap:10px;align-items:flex-start}.cta small{color:var(--ink-3);font-weight:600}
@media (max-width:640px){.cta .btn{width:100%}}
.trust{display:flex;flex-wrap:wrap;gap:8px 22px;margin:26px 0 0;padding:0;list-style:none;font-weight:700;color:var(--ink-2);font-size:.95rem}
.trust li::before{content:"✓ ";color:var(--ok);font-weight:900}
.offer{background:var(--ink);color:#fff;border-radius:22px;padding:28px;box-shadow:0 24px 60px rgba(11,30,63,.18)}
.offer .k{font-weight:700;color:var(--mark);font-size:.9rem;text-transform:uppercase;letter-spacing:.06em}
.offer .amt{font-size:clamp(2.6rem,5vw,3.6rem);font-weight:900;letter-spacing:-.04em;line-height:1;margin-top:10px}
.offer .amt small{font-size:1rem;font-weight:700;letter-spacing:0;color:#C9D3E6;margin-left:8px}
.offer ul{margin:18px 0 0;padding:0;list-style:none;display:grid;gap:10px;color:#E3E9F4;font-size:1rem}
.offer li::before{content:"✓ ";color:var(--mark);font-weight:900}
.offer .g{margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,.14);font-weight:700}
.offer .g b{color:var(--mark)}
.offer .btn{width:100%;margin-top:18px}
.offer .tel{display:block;text-align:center;margin-top:12px;color:#C9D3E6;font-weight:700;font-size:.95rem}
.strip{background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding-block:22px}
.strip .wrap{display:flex;flex-wrap:wrap;gap:10px 32px;justify-content:center;font-weight:700;color:var(--ink-2);font-size:.98rem}
.strip span::before{content:"✓ ";color:var(--ok);font-weight:900}
.letter{background:var(--surface)}
.letter .wrap{display:grid;grid-template-columns:.7fr 1.3fr;gap:44px;align-items:start}
@media (max-width:860px){.letter .wrap{grid-template-columns:1fr;gap:24px}}
.letter .mono{aspect-ratio:4/5;border-radius:22px;background:var(--ink);display:grid;place-content:center;text-align:center;padding:24px;color:#fff;position:sticky;top:92px}
.letter .mono span{font-size:clamp(3.6rem,9vw,6rem);font-weight:900;letter-spacing:-.05em;line-height:1;color:var(--mark)}
.letter .mono small{display:block;margin-top:12px;font-weight:700;color:#C9D3E6}
@media (max-width:860px){.letter .mono{aspect-ratio:16/6;position:static}}
.letter p{color:var(--ink-2);font-size:1.08rem;max-width:60ch}.letter p+p{margin-top:14px}
.letter .sig{margin-top:22px;font-weight:800;color:var(--ink)}.letter .sig small{display:block;font-weight:600;color:var(--ink-3)}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
@media (max-width:860px){.grid3{grid-template-columns:1fr}}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:24px}
.card .n{width:36px;height:36px;border-radius:10px;background:var(--mark);color:var(--ink);font-weight:900;display:grid;place-content:center;margin-bottom:14px}
.card h3{margin-bottom:8px}.card p{color:var(--ink-2);font-size:1rem}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:30px}
@media (max-width:760px){.two{grid-template-columns:1fr}}
.two .card ul{margin:12px 0 0;padding-left:0;list-style:none;color:var(--ink-2);font-size:1rem;display:grid;gap:8px}
.two .yes li::before{content:"✓ ";color:var(--ok);font-weight:900}.two .no li::before{content:"— ";color:var(--ink-3);font-weight:900}
.guar{background:var(--ink);color:#fff}
.guar .kicker{color:var(--mark)}
.guar .box{display:grid;grid-template-columns:1.1fr .9fr;gap:36px;align-items:center}
@media (max-width:820px){.guar .box{grid-template-columns:1fr}}
.guar p{color:#C9D3E6;font-size:1.1rem;margin-top:18px;max-width:52ch}
.guar .big{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:28px}
.guar .big b{display:block;font-size:clamp(2.6rem,5vw,4rem);font-weight:900;letter-spacing:-.04em;line-height:1;color:var(--mark)}
.guar .big span{display:block;margin-top:10px;font-weight:700;font-size:1.1rem}
.faq details{border-top:1px solid var(--line);padding:16px 0}.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;font-weight:800;font-size:1.08rem;list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::after{content:"+";color:var(--accent);font-weight:900}.faq details[open] summary::after{content:"–"}
.faq p{margin-top:10px;color:var(--ink-2);max-width:66ch}
.final{text-align:center}
.final .btn{margin-top:26px}
.final .sub{margin-top:14px;color:var(--ink-3);font-weight:600}
footer{border-top:1px solid var(--line);padding:28px 0 calc(28px + 80px);color:var(--ink-3);font-size:.9rem}
footer .wrap{display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:space-between}
footer a{color:var(--ink-2);text-decoration:none;font-weight:600}
.sticky{display:none}
@media (max-width:860px){
  .sticky{display:flex;gap:10px;position:fixed;left:0;right:0;bottom:0;z-index:10;padding:10px max(16px,env(safe-area-inset-right,0px)) calc(10px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));background:rgba(255,255,255,.96);backdrop-filter:blur(8px);border-top:1px solid var(--line)}
  .sticky .btn{flex:1;padding:14px 10px;font-size:1rem}.sticky .btn.ghost{flex:0 0 auto}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="/"><span class="mk" aria-hidden="true"></span>Margin Digital</a>
    <a class="call" href="__TEL__">Call __PHONE__</a>
    <a class="btn" href="__CAL__" target="_blank" rel="noopener">Book a free 30-minute call</a>
  </div>
</header>
<main>
"""

FOOT = """</main>
<footer>
  <div class="wrap">
    <div>© Margin Digital · Sydney, Australia · <a href="mailto:hello@margindigital.com.au">hello@margindigital.com.au</a> · <a href="__TEL__">__PHONE__</a></div>
    <div><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a></div>
  </div>
</footer>
<div class="sticky">
  <a class="btn ghost" href="__TEL__" aria-label="Call __PHONE__">Call</a>
  <a class="btn" href="__CAL__" target="_blank" rel="noopener">Book a free call</a>
</div>
<script>
document.addEventListener('click',function(e){var a=e.target.closest('a[href*="calendly.com"]');if(a&&window.gtag){gtag('event','conversion',{'send_to':'AW-18536302130/KGlTCJmvlKkdELKM5oZF'});}var t=e.target.closest('a[href^="tel:"]');if(t&&window.gtag){gtag('event','conversion',{'send_to':'AW-18536302130/4WSZCLryz6kdELKM5oZF','value':1.0,'currency':'AUD'});}});
</script>
</body>
</html>
"""

def cta(label="Book a free 30-minute call", sub="No pitch deck. Thirty minutes on your business, then you decide."):
    return f'''<div class="cta"><a class="btn" href="{CAL}" target="_blank" rel="noopener">{label}</a><small>{sub}</small></div>'''

def hero(pill, h1, lead, offer_html, trust):
    return f'''<section class="hero">
  <div class="wrap">
    <div>
      <div class="pill"><i></i>{pill}</div>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      {cta()}
      <ul class="trust">{''.join(f'<li>{t}</li>' for t in trust)}</ul>
    </div>
    {offer_html}
  </div>
</section>'''

def offer(k, amt, per, bullets, guarantee):
    return f'''<aside class="offer" aria-label="Pricing">
      <div class="k">{k}</div>
      <div class="amt">{amt}<small>{per}</small></div>
      <ul>{''.join(f'<li>{b}</li>' for b in bullets)}</ul>
      <div class="g">{guarantee}</div>
      <a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a free 30-minute call</a>
      <a class="tel" href="{TEL}">Prefer to talk now? {PHONE}</a>
    </aside>'''

STRIP = '''<div class="strip"><div class="wrap"><span>Fixed prices, published upfront</span><span>Full money-back guarantee</span><span>Founder-led, Sydney based</span><span>You own every account and asset</span></div></div>'''

def call_section():
    return f'''<section>
  <div class="wrap">
    <p class="kicker">What the call actually is</p>
    <h2>Thirty minutes, with the person who would do the work.</h2>
    <p class="lead" style="margin-top:16px">It is not a sales call with a closer. It is me, looking at your business with you. Here is how it goes.</p>
    <div class="grid3">
      <div class="card"><div class="n">1</div><h3>You tell me what you want more of</h3><p>Which jobs, which customers, which suburbs. What a good month looks like, and what has been tried before.</p></div>
      <div class="card"><div class="n">2</div><h3>I show you what I would do</h3><p>Before the call I look at your website, your Google listing and what your competitors are running. On the call you get the plan, in plain English, whether or not you hire me.</p></div>
      <div class="card"><div class="n">3</div><h3>You decide, with nothing to lose</h3><p>If it makes sense, we start. If you are not happy at any point afterwards, you get every dollar back. If it does not make sense, you still leave with the plan.</p></div>
    </div>
    {cta("Book my free 30-minute call", "Pick a time that suits. I take the call personally.")}
  </div>
</section>'''

def letter(h2, paras):
    return f'''<section class="letter">
  <div class="wrap">
    <div class="mono"><span>MD</span><small>Founder-led</small></div>
    <div>
      <p class="kicker">A note from the founder</p>
      <h2>{h2}</h2>
      <div style="margin-top:18px">{''.join(f'<p>{p}</p>' for p in paras)}</div>
      <div class="sig">Joel<small>Founder, Margin Digital · {PHONE}</small></div>
    </div>
  </div>
</section>'''

def fit(yes, no):
    return f'''<section>
  <div class="wrap">
    <p class="kicker">Is this for you?</p>
    <h2>I would rather tell you now than waste your thirty minutes.</h2>
    <div class="two">
      <div class="card yes"><h3>A good fit if</h3><ul>{''.join(f'<li>{y}</li>' for y in yes)}</ul></div>
      <div class="card no"><h3>Probably not the right fit if</h3><ul>{''.join(f'<li>{n}</li>' for n in no)}</ul></div>
    </div>
  </div>
</section>'''

def guarantee(h2, p, big, sub):
    return f'''<section class="guar">
  <div class="wrap">
    <div class="box">
      <div>
        <p class="kicker">The guarantee</p>
        <h2>{h2}</h2>
        <p>{p}</p>
      </div>
      <div class="big"><b>{big}</b><span>{sub}</span></div>
    </div>
  </div>
</section>'''

def faq(items):
    return f'''<section class="faq">
  <div class="wrap">
    <p class="kicker">Questions people ask on the call</p>
    <h2 style="margin-bottom:24px">Straight answers.</h2>
    {''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)}
  </div>
</section>'''

def final(h2, sub):
    return f'''<section class="final">
  <div class="wrap">
    <h2>{h2}</h2>
    <a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a free 30-minute call</a>
    <p class="sub">{sub} · or call <a href="{TEL}" style="font-weight:800;color:var(--ink)">{PHONE}</a></p>
  </div>
</section>'''

def page(title, desc, body):
    h = HEAD.replace("__TITLE__", html.escape(title)).replace("__DESC__", html.escape(desc))
    s = h + body + FOOT
    return s.replace("__TEL__", TEL).replace("__PHONE__", PHONE).replace("__CAL__", CAL)

COMMON_FAQ = [
    ("What does the call cost?", "Nothing. Thirty minutes, no obligation, and you keep the plan either way."),
    ("How does the money-back guarantee work?", "If at any point you decide Margin Digital is not for you, say so and every dollar you have paid us is refunded. You keep everything that was built or set up. Ad spend is paid by you directly to Google and Meta and is not part of what we charge."),
    ("Who actually does the work?", "I do. I am the person you speak to on the call, the person building and running the account, and the person you text when something comes up. There is no account manager in between."),
    ("Do I have to sign a contract?", "No lock-in. Monthly plans are month to month and you can stop any month. The website is a one-off fee."),
    ("Is there anything extra to pay?", "Advertising spend goes directly to Google and Meta from your own account. Hosting and any third-party subscriptions are separate and itemised up front, so there are no surprises on the invoice."),
    ("Do you work outside Sydney?", "Yes. Margin Digital is Sydney based and works with businesses across Australia. Everything is done online and by phone."),
]

# ---------------- /website ----------------
WEBSITE = (
    hero(
        "Taking 5 founding clients at $2,500",
        "A website that turns the people who find you into enquiries.",
        "Most small business websites look fine and do nothing. Yours should make the phone ring. I build it for a fixed $2,500, you deal directly with me, and if you are not happy at any point you get every dollar back.",
        offer("Website design", "$2,500", "once, AUD ex GST",
              ["Designed and written for your business, not a template",
               "Built mobile-first with call, booking and enquiry wired to your phone",
               "Google Business Profile set up alongside it",
               "Every asset in your name: domain, site, listing",
               "Founding client rate, locked in"],
              "<b>Full money-back guarantee.</b> Not happy at any point? Every dollar back, and you keep the site."),
        ["Fixed price, no monthly fees for the site", "Built by a business owner", "Sydney based, Australia wide"],
    )
    + STRIP
    + call_section()
    + letter(
        "I have paid for websites that did nothing. That is why I build them differently.",
        ["I run my own business. Before Margin Digital I hired agencies to build sites and run ads for me, spent real money, and was let down by more than one of them. Beautiful pages, long reports, very few enquiries.",
         "So when I build a website now, I start from the only question that matters: when someone lands on this page from Google at 7pm with a problem, what gets them to call? That decides the layout, the words, the buttons and what goes above the fold on a phone.",
         "You will not be handed to an account manager. You get my mobile number, you see the site before it goes live, and if you are not happy at any point you get every dollar back. I can afford to offer that because I am confident in the work, and because I would rather have a happy client than a signed contract."],
    )
    + fit(
        ["You are a trade, clinic, gym, salon or local service and one new customer is worth more than the build",
         "Your current site is old, slow, built by a mate, or does not exist yet",
         "You want one fixed price and one person to deal with",
         "You answer the phone when it rings"],
        ["You need a large e-commerce store or custom software",
         "You want the cheapest possible site rather than one that gets enquiries",
         "You are not able to supply a logo, some photos and a list of your services"],
    )
    + guarantee(
        "Not happy at any point? Every dollar back.",
        "That is the whole guarantee, in one sentence. No conditions buried in a contract, no partial refunds. If you decide Margin Digital is not for you, say so and you are refunded in full. You keep the site, the domain and the listing.",
        "100%", "money back, any time, and you keep the work",
    )
    + faq([("What is included in the $2,500?", "A complete website designed and written for your business, built to convert on a phone, with your calls, bookings and enquiry form wired to you, plus your Google Business Profile set up alongside it. Hosting and third-party subscriptions are separate and itemised up front.")] + COMMON_FAQ)
    + final("Thirty minutes with me. A plan either way.", "No obligation. Founding client rate held for the first five.")
)

# ---------------- /ads ----------------
ADS = (
    hero(
        "Taking 5 founding clients at $799/mo",
        "Google Ads for your business, run by someone who has spent his own money on them.",
        "A flat $799 a month, not a percentage of your spend. Leads, not vanity metrics. You own the account and the data, you get a report you can actually read, and if you are not happy at any point, every dollar back.",
        offer("Google Ads or Meta Ads", "$799", "per month, AUD ex GST",
              ["Flat fee, not a percentage of ad spend",
               "Your own ad account, your data, no lock-in",
               "Conversion tracking on calls and forms from day one",
               "Clear monthly reporting: enquiries and cost per enquiry",
               "Google + Meta together: $1,299/mo"],
              "<b>Full money-back guarantee.</b> Unhappy at any point? Every dollar we have charged is refunded."),
        ["No lock-in contracts", "Run by a business owner", "Trades, clinics, gyms and local services"],
    )
    + STRIP
    + call_section()
    + letter(
        "I know what it is like to pay an agency and not know what you got.",
        ["I run my own business and I have hired agencies to run my ads. I have paid retainers, waited for the monthly report, and still not been able to answer the only question that mattered: what did a new customer cost me?",
         "That is why Margin Digital charges a flat fee instead of a percentage of your spend. When an agency earns more as your budget grows, the incentive is to grow the budget. When I earn a flat $799, the only way I keep you as a client is to make the ads pay for themselves.",
         "Every account is set up in your name with conversion tracking on calls and forms from the first click. Each month you get one page: what was spent, how many enquiries came in, what each one cost, and what I am changing next. If you ever want to leave, the account, the data and the history go with you. And if you are not happy at any point, every dollar is refunded."],
    )
    + fit(
        ["You are a trade, clinic, gym, salon or local service and a new customer is worth a few hundred dollars or more",
         "You can commit a real ad budget alongside the management fee and give it a few months to compound",
         "You want to know your cost per enquiry, not your impressions",
         "You answer the phone and follow up the leads"],
        ["You are looking for the cheapest possible clicks regardless of quality",
         "Your business cannot take on more work right now",
         "You want a guaranteed number of leads in the first week"],
    )
    + guarantee(
        "Unhappy at any point? Every dollar we charged, back.",
        "No conditions, no minimum term, no partial refunds. If you decide Margin Digital is not for you, say so and the management fees you have paid are refunded in full. The ad account, the data and the campaigns stay with you.",
        "100%", "of management fees refunded, any time",
    )
    + faq([
        ("Does the $799 include the ad spend?", "No. Ad spend is paid by you directly to Google or Meta from your own account, so you can see every dollar. The $799 covers the strategy, build, management, tracking and reporting."),
        ("How much ad spend do I need?", "It depends on your industry and suburb, and that is one of the things we work out on the call. I will give you a realistic figure based on what the clicks cost in your market rather than a number pulled from the air."),
        ("Google or Meta, which should I run?", "For most trades and clinics, Google first, because people are searching with intent. Gyms, studios and salons often do well on Meta. Running both together is $1,299 a month and lets us see which channel produces the cheaper enquiry."),
    ] + COMMON_FAQ)
    + final("Thirty minutes with me. A plan for your ads either way.", "No obligation. Founding client rate held for the first five.")
)

# ---------------- /start (general) ----------------
START = (
    hero(
        "Taking 5 founding clients",
        "More enquiries for your business, from someone who has been on your side of the table.",
        "Websites, Google Ads and Meta Ads for trades, clinics, gyms and local services. Fixed prices published upfront, one person doing the work, and a full money-back guarantee if you are not happy at any point.",
        offer("Founding client pricing", "$2,500", "website, once",
              ["Google Ads $799/mo or Meta Ads $799/mo",
               "Complete Growth (both): $1,299/mo",
               "Flat fees, not a percentage of ad spend",
               "No lock-in. Every asset in your name",
               "Rates locked in for life for founding clients"],
              "<b>Full money-back guarantee.</b> Not happy at any point? Every dollar back."),
        ["Fixed prices, no surprises", "Built and run by a business owner", "Sydney based, Australia wide"],
    )
    + STRIP
    + call_section()
    + letter(
        "I started this because I was let down by agencies. More than once.",
        ["I have built businesses, spent my own money on advertising and hired agencies to do what I now do. Some were fine. Several were not. The pattern was always the same: a confident pitch, a long report, and no clear line between what I paid and what I got back.",
         "What I learned is that good marketing is not a ROAS figure on a slide. It shows up in the health of the business: what a customer costs to acquire, what they are worth, and whether they come back. I understand those numbers because I have had my own money on the line against them.",
         "Margin Digital is deliberately small. You deal with me, your prices are on the page before you call, every account is in your name, and if you are not happy at any point you get every dollar back. That is the agency I wanted to hire. It did not exist, so I built it."],
    )
    + fit(
        ["You run a trade, clinic, gym, studio, salon or local service",
         "One new customer is worth more to you than a month of this",
         "You want one person, one price and a report you can read",
         "You answer the phone when it rings"],
        ["You want the cheapest option rather than the one that gets enquiries",
         "You need enterprise software or a large online store",
         "You are not in a position to take on more work"],
    )
    + guarantee(
        "Not happy at any point? Every dollar back.",
        "One sentence, no fine print. If you decide Margin Digital is not for you, say so and you are refunded in full. You keep the website, the listing, the ad accounts and the data.",
        "100%", "money back, any time, and you keep everything",
    )
    + faq([("Which service should I start with?", "That is what the call is for. If your website is not converting, we start there, because ads sent to a weak page waste money. If the site is sound, we start with Google Ads. I will tell you honestly which one, even if it is the cheaper option.")] + COMMON_FAQ)
    + final("Thirty minutes with me. A plan either way.", "No obligation. Founding client rates held for the first five.")
)

out = pathlib.Path("public")
(out / "website.html").write_text(page("Website design, $2,500 fixed — Margin Digital", "A website built to turn visitors into enquiries. Fixed $2,500, built by a business owner, full money-back guarantee. Book a free 30-minute call.", WEBSITE))
(out / "ads.html").write_text(page("Google Ads management, $799/mo flat — Margin Digital", "Google and Meta Ads managed for a flat $799/month by a business owner. Your account, your data, full money-back guarantee. Book a free 30-minute call.", ADS))
(out / "start.html").write_text(page("More enquiries for your business, or every dollar back — Margin Digital", "Websites, Google Ads and Meta Ads for local businesses. Fixed prices, founder-led, full money-back guarantee. Book a free 30-minute call.", START))
print("built")
