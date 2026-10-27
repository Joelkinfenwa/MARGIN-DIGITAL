import json,re,sys,html
src=open('public/p/plumbers-please.html').read()
g1=src[src.index('<script>'):src.index('</script>')+9]
g2=src[src.index('<script>',src.index('<div class="sticky"')):src.index('</script>',src.index('<div class="sticky"'))+9]
TPL=open('public/p/plumbers-please.html').read()

def build(c):
    s=TPL
    rep={
     'https://plumbersplease.net.au/wp-content/uploads/2023/09/Plumbers-Please_Logos-01-BLEND.svg':c['logo'],
     '--blue:#00B2E2;--navy:#1D51A4':f"--blue:{c['c1']};--navy:{c['c2']}",
     "font-family:Poppins,Arial,Helvetica,sans-serif":f"font-family:{c['font']},Arial,Helvetica,sans-serif",
     'family=Poppins:wght@400;500;600;700;800':f"family={c['font'].replace(' ','+')}:wght@400;500;600;700;800",
     '<title>Plumbers Please on Google — a preview</title>':f"<title>{c['name']} on Google — a preview</title>",
     'alt="Plumbers Please"':f'alt="{c["name"]}"',
    }
    for a,b in rep.items(): s=s.replace(a,b)
    # hero
    s=re.sub(r'<h1>.*?</h1>',f"<h1>{c['h1']}</h1>",s,count=1,flags=re.S)
    s=re.sub(r'<p class="lead">Below is a working preview.*?</p>',f"<p class=\"lead\">{c['lead']}</p>",s,count=1,flags=re.S)
    s=re.sub(r'<div class="facts">.*?</div>\s*</div>\s*</div>\s*<div class="note">',
             '<div class="facts">'+''.join(f'<div class="fact"><b>{a}</b><span>{b}</span></div>' for a,b in c['facts'])+'</div><div class="note">',s,count=1,flags=re.S)
    s=re.sub(r'<div class="note">.*?</div>',f"<div class=\"note\"><strong>Why you, specifically.</strong> {c['why']}</div>",s,count=1,flags=re.S)
    # phone mock
    s=s.replace('emergency plumber sutherland shire</div></div>',f"{c['q1']}</div></div>")
    s=s.replace('<div>Plumbers Please<small>plumbersplease.net.au</small></div>',f"<div>{c['name']}<small>{c['domain']}</small></div>")
    s=re.sub(r'<div class="hl">Emergency Plumber Sutherland Shire.*?</div>',f"<div class=\"hl\">{c['ad1h']}</div>",s,count=1,flags=re.S)
    s=s.replace('5.0 · 94 Google reviews',f"{c['rating']} · {c['reviews']} Google reviews")
    s=re.sub(r'<div class="ds">Local Caringbah plumbers.*?</div>',f"<div class=\"ds\">{c['ad1d']}</div>",s,count=1,flags=re.S)
    s=s.replace('📞 Call 0413 327 408',f"📞 Call {c['phone']}")
    s=s.replace('Call 0413 327 408',f"Call {c['phone']}").replace('rings 0413 327 408',f"rings {c['phone']}")
    # four search cards
    cards=''.join(f'<div class="card"><div class="q">They search: <b>"{q}"</b></div><div class="ad"><div class="u"><b>Sponsored</b> · {c["domain"]}{p}</div><div class="h">{h}</div><div class="d">{d}</div></div></div>' for q,p,h,d in c['cards'])
    s=re.sub(r'<div class="grid">.*?</div>\s*<p class="hon">','<div class="grid">'+cards+'</div><p class="hon">',s,count=1,flags=re.S)
    s=s.replace('Each ad group sends people to the page on plumbersplease.net.au',f"Each ad group sends people to the page on {c['domain']}")
    # schedule/suburbs
    s=re.sub(r'<p class="lead">Targeted suburb by suburb.*?</p>',f"<p class=\"lead\">{c['sched_lead']}</p>",s,count=1,flags=re.S)
    s=re.sub(r'<div class="chips">.*?</div>','<div class="chips">'+''.join(f'<span>{x}</span>' for x in c['suburbs'])+'</div>',s,count=1,flags=re.S)
    bar=''.join('<i class="%s"></i>'%('hi' if h in c['peak'] else 'on' if h in c['on'] else '') for h in range(24))
    s=re.sub(r'<div class="bar">.*?</div>','<div class="bar">'+bar+'</div>',s,count=1,flags=re.S)
    s=s.replace('Dark blue: peak bids 6 to 9am. Light blue: on. Grey: off.',c['bar_note'])
    s=re.sub(r'<img class="team"[^>]*>', (f'<img class="team" src="{c["photo"]}" alt="{c["name"]}">' if c.get('photo') else ''),s)
    # report rows
    rows=''.join(f'<tr><td>{a}</td><td>{b}</td><td>{d}</td><td>{e}</td><td><span class="tag {t}">{o}</span></td></tr>' for a,b,d,e,t,o in c['rows'])
    s=re.sub(r'<tr><th>When</th>.*?</table>','<tr><th>When</th><th>Search</th><th>Suburb</th><th>Length</th><th>Outcome</th></tr>'+rows+'</table>',s,count=1,flags=re.S)
    s=s.replace('Plumbers Please · Google Ads calls',f"{c['name']} · Google Ads calls")
    s=s.replace('With 244 five-star reviews','')
    s=s.replace('A sensible start for the Shire is $100 to $150 a day',c.get('budget','A sensible start is $100 to $150 a day'))
    s=s.replace('I have not worked with Plumbers Please',f"I have not worked with {c['name']}")
    s=s.replace('Prepared privately for Plumbers Please',f"Prepared privately for {c['name']}").replace('Logo and photo belong to Plumbers Please Pty Ltd','Logo and photo belong to '+c['name'])
    s=s.replace('Plumbers Please',c['name'])
    open(f"public/p/{c['slug']}.html",'w').write(s)
    print('built',c['slug'])

C=[
dict(slug='mpj-plumbing',name='MPJ Plumbing Group',domain='mpjplumbing.com.au',logo='https://e7ff60c4.delivery.rocketcdn.me/wp-content/uploads/MPJ-logo-240x120-1.webp',c1='#64A10D',c2='#0170B9',font='Montserrat',
 phone='(02) 8537 3316',rating='5.0',reviews='269',
 h1='When a strata manager or a homeowner in the Shire searches for a plumber, MPJ Plumbing Group should be the first result they see.',
 lead='Below is a working preview of the campaign: the actual searches, the ads written for you, where the calls go, the hours it runs and what the report looks like. Nothing here needs a new website. It runs on mpjplumbing.com.au and rings (02) 8537 3316.',
 facts=[('269','Google reviews, all five stars'),('24/7','emergency and planned maintenance'),('2','markets: residential and strata/commercial')],
 why='Google Ads rewards three things: a strong review profile, a site that gets people to the phone or the booking form, and the ability to attend the same day. MPJ has all three, plus a commercial and strata offer that almost nobody else in the Shire is advertising for. That is why this page is about Ads only; the site is already doing its job.',
 q1='plumber taren point',ad1h='Plumber Taren Point | 269 Five-Star Reviews | Same-Day, Clear Pricing',ad1d='Licensed Sydney plumbers based in Taren Point. Emergency call-outs 24/7, planned maintenance, strata and commercial. Clear pricing before work starts.',
 cards=[('emergency plumber sutherland shire','','Emergency Plumber Sutherland Shire | 24/7 | MPJ Plumbing Group','Burst pipes, blocked drains and no hot water, attended 24/7 across the Shire. 269 five-star reviews. Call (02) 8537 3316.'),
        ('strata plumber sydney',' › commercial','Strata Plumbing Sydney | Planned Maintenance and Reporting','Site assessment, agreed scheduling and service reporting for strata and commercial properties. Prevent problems before they disrupt the building.'),
        ('blocked drain taren point',' › blocked-drains','Blocked Drains and CCTV Inspection | MPJ Plumbing Taren Point','Same-day clearing with camera inspection so you know the cause. Pipe relining available. Clear pricing, five-star rated.'),
        ('hot water repair sutherland shire',' › hot-water','Hot Water Repairs and Installs | Sutherland Shire | MPJ Plumbing','Repairs, replacements and new installs, same day where possible. Licensed, local, 269 five-star reviews. Call now.')],
 sched_lead='Two campaigns. Residential: targeted suburb by suburb across the Shire, 24 hours for emergency searches with bids raised 6am to 9am and 4pm to 8pm. Strata and commercial: Sydney-wide, business hours only, landing on your commercial page.',
 suburbs=['Taren Point','Caringbah','Miranda','Cronulla','Gymea','Kirrawee','Sutherland','Sylvania','Engadine','Menai','Jannali','Como','Oyster Bay','Illawong','Bangor','Sydney (strata and commercial)'],
 peak=list(range(6,9))+list(range(16,20)),on=[h for h in range(24) if h not in list(range(6,9))+list(range(16,20))],bar_note='Dark blue: peak bids 6 to 9am and 4 to 8pm. Light blue: on. Residential runs 24 hours to match your emergency service.',
 photo='',rows=[('Mon 6:50am','burst pipe caringbah','Caringbah','3:40','j','Job booked'),('Mon 10:15am','strata plumber sydney','Sydney','6:12','q','Quote requested'),('Tue 8:05am','no hot water sutherland shire','Gymea','2:55','j','Job booked'),('Wed 5:20pm','blocked drain taren point','Taren Point','0:48','m','Missed, called back')],
 budget='A sensible start is $100 to $150 a day for residential and $50 a day for strata and commercial'),
dict(slug='eagle-plumbing',name='Eagle Plumbing 24/7',domain='eagleplumbing247.com.au',logo='https://eagleplumbing247.com.au/eagle-plumbing-logo.webp',c1='#E60F0F',c2='#0F1729',font='Inter',
 phone='0489 998 221',rating='5.0',reviews='104',
 h1='At midnight with a burst pipe, the person searching "emergency plumber near me" in the Shire should see Eagle Plumbing 24/7 first.',
 lead='Below is a working preview of the campaign: the actual searches, the ads written for you, where the calls go, the hours it runs and what the report looks like. Nothing here needs a new website. It runs on eagleplumbing247.com.au and rings 0489 998 221.',
 facts=[('104','Google reviews, all five stars'),('24/7','genuinely, not 6am to 6pm'),('$0','call-out fee, lifetime workmanship guarantee')],
 why='Most plumbers advertising in the Shire switch their ads off overnight. You do not switch your trucks off, so the after-hours emergency searches, which are the most urgent and least contested, are yours to own. Add 104 five-star reviews and a $0 call-out fee and the ad writes itself.',
 q1='emergency plumber near me',ad1h='24 Hour Emergency Plumber | On Our Way Now | $0 Call-Out Fee',ad1d='Family-owned Shire plumbers, available right now. Burst pipes, blocked drains, no hot water. 104 five-star reviews, lifetime workmanship guarantee. Call 0489 998 221.',
 cards=[('after hours plumber sutherland shire','','After Hours Plumber Sutherland Shire | Eagle Plumbing 24/7','We answer at 2am and we turn up. $0 call-out, 15% off for first-time customers. Family owned, five-star rated.'),
        ('burst pipe plumber cronulla',' › burst-pipes','Burst Pipe? Cronulla Plumber On The Way | 24/7 | $0 Call-Out','Fast response across Cronulla, Burraneer and the Shire. Lifetime workmanship guarantee. Call now, we are available.'),
        ('blocked drain cronulla',' › blocked-drains','Blocked Drain Cronulla | Same Day or Tonight | Eagle Plumbing','Sinks, showers, toilets and sewers cleared any hour. $0 call-out fee, 104 five-star reviews. Tap to call.'),
        ('hot water repair near me',' › hot-water','No Hot Water? Repaired Tonight | 24/7 Shire Plumbers','Repairs and replacements across the Sutherland Shire, any hour. $150 cash back on hot water this month. Call 0489 998 221.')],
 sched_lead='Targeted suburb by suburb across the Shire and running 24 hours, because you do. Bids raised from 8pm to 7am, when most competitors are off and the searches are most urgent.',
 suburbs=['Burraneer','Cronulla','Caringbah','Miranda','Woolooware','Gymea','Kirrawee','Sutherland','Sylvania','Engadine','Menai','Jannali','Como','Oyster Bay','Illawong','Bangor'],
 peak=list(range(20,24))+list(range(0,7)),on=list(range(7,20)),bar_note='Dark blue: peak bids 8pm to 7am, the after-hours window. Light blue: on. Never off.',
 photo='',rows=[('Sun 11:40pm','emergency plumber near me','Cronulla','2:58','j','Job booked'),('Mon 1:15am','burst pipe plumber','Caringbah','4:02','j','Job booked'),('Tue 7:30am','blocked drain cronulla','Woolooware','1:50','q','Quote requested'),('Wed 9:05pm','no hot water sutherland shire','Miranda','0:35','m','Missed, called back')],
 budget='A sensible start is $100 to $150 a day, with most of it spent after hours'),
dict(slug='ezyflow',name='Ezyflow H2O Plumbing Solutions',domain='ezyflowh2o.com.au',logo='https://ezyflowh2o.com.au/wp-content/uploads/2024/05/rsw-643h-500cg-true.webp',c1='#2EA3F2',c2='#1B3A6B',font='Poppins',
 phone='0415 743 200',rating='5.0',reviews='80',
 h1='When someone in Menai or Illawong searches for a plumber, Ezyflow H2O should be the first name they see.',
 lead='Below is a working preview of the campaign: the actual searches, the ads written for you, where the calls go, the hours it runs and what the report looks like. Nothing here needs a new website. It runs on ezyflowh2o.com.au and rings 0415 743 200.',
 facts=[('80','Google reviews, all five stars'),('6','services already on your site'),('Menai','based, with the west of the Shire on your doorstep')],
 why='The west side of the Shire (Menai, Illawong, Bangor, Alfords Point, Barden Ridge) is searched every day and most of the plumbers advertising for it are based in Caringbah or Cronulla. A Menai-based plumber with 80 five-star reviews is the obvious choice for those searches, if the ad is there when they look.',
 q1='plumber menai',ad1h='Plumber Menai | Local, 80 Five-Star Reviews | Ezyflow H2O',ad1d='Menai-based plumbers for blocked drains, hot water, leaks, gas and pipe relining. Fast local response across the western Shire. Call 0415 743 200.',
 cards=[('emergency plumber menai','','Emergency Plumber Menai and Illawong | Ezyflow H2O','Burst pipes, blocked drains and no hot water across the western Shire. Local, licensed, five-star rated. Call now.'),
        ('blocked drain menai',' › blocked-drains','Blocked Drains Menai | Cleared Fast | Ezyflow H2O Plumbing','Sinks, showers, toilets and sewers cleared. Camera inspection and pipe relining available. 80 five-star reviews.'),
        ('leak detection sutherland shire',' › leak-detection','Leak Detection Sutherland Shire | Find It Without Digging','Hidden leaks found and fixed. Water bill up or damp patches? Local Menai plumbers, five-star rated. Call 0415 743 200.'),
        ('hot water repair menai',' › hot-water','Hot Water Repairs Menai | Same Day | Ezyflow H2O','Repairs and replacements for all systems. Local, licensed, 80 five-star reviews. Call now.')],
 sched_lead='Targeted suburb by suburb with the western Shire first, then the rest. Ads run during your service hours, with bids raised 6am to 9am and 4pm to 7pm when home-plumbing searches peak.',
 suburbs=['Menai','Illawong','Bangor','Alfords Point','Barden Ridge','Lucas Heights','Woronora','Sutherland','Jannali','Como','Oyster Bay','Engadine','Kirrawee','Gymea','Miranda'],
 peak=list(range(6,9))+list(range(16,19)),on=list(range(9,16))+[19,20],bar_note='Dark blue: peak bids 6 to 9am and 4 to 7pm. Light blue: on. Grey: off. Hours are set to match yours.',
 photo='',rows=[('Mon 7:10am','plumber menai','Menai','3:05','j','Job booked'),('Mon 4:45pm','blocked drain illawong','Illawong','2:20','j','Job booked'),('Tue 8:30am','leak detection sutherland shire','Bangor','5:10','q','Quote requested'),('Thu 6:15pm','hot water repair menai','Menai','0:40','m','Missed, called back')]),
]
for c in C: build(c)
