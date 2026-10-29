import html
NAV=[("index.html","Home"),("planners.html","Planners"),("regalia.html","Ph.D. Regalia"),("save-checklist.html","Free SAVE Checklist"),("app.html","App"),("about.html","About"),("contact.html","Contact")]
def page(fn,title,desc,body):
    nav="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Grad-IQ</title><meta name="description" content="{html.escape(desc)}"><link rel="icon" href="assets/img/favicon.svg"><link rel="stylesheet" href="assets/site.css"></head><body>
<header><div class="wrap bar"><a class="brand" href="index.html"><img src="assets/img/iq-learning-logo.png" alt="IQ Learning logo"><span>Grad-IQ<small>by IQLearning LLC</small></span></a>
<button class="menu" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main>{body}</main>
<footer><div class="wrap cols"><div>© 2026 IQLearning LLC · Las Vegas, NV<br><a href="mailto:jay.s@grad-iq.org">jay.s@grad-iq.org</a></div>
<ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV[1:])}<li><a href="privacy.html">Privacy</a></li></ul></div></footer>
<script src="assets/config.js"></script><script src="assets/site.js"></script></body></html>'''
P=[("open-enrollment","Open Enrollment Health-Cost Planner","https://gradiq.github.io/open-enrollment-planner/","Compare health-plan options and estimate your yearly costs before open enrollment closes."),
("beat-rising-prices","Beat Rising Prices Budget Planner","https://gradiq.github.io/beat-rising-prices-planner/","Track cash flow, triage spending and plan around higher everyday costs."),
("phd-stipend-loan","PhD Stipend & Loan Budget Planner","https://gradiq.github.io/phd-stipend-loan-planner/","Budget your stipend month by month, spot gaps, and keep student loans in view."),
("burnout-proof-study","Burnout-Proof Study Tracker","https://gradiq.github.io/burnout-proof-study-tracker/","Plan today's focus, run study sessions and review with cards, without burning out."),
("phd-roadmap","PhD Roadmap Planner","https://gradiq.github.io/phd-roadmap-planner/","Map milestones, advisor meetings and deadlines from coursework to defense.")]
cards="".join(f'''<article class="card"><img class="shot" src="assets/img/{s}.png" alt="{html.escape(t)} demo on a phone" loading="lazy"><h3>{html.escape(t)}</h3><p>{d}</p><div class="spacer"></div>
<p class="price">$19</p><div class="btns"><a class="btn" href="{u}" target="_blank" rel="noopener">Try the demo</a><a class="btn disabled" data-buy="{s}" aria-disabled="true">Coming soon to Etsy</a></div></article>''' for s,t,u,d in P)
pages={}
pages["index.html"]=("Home","Grad-IQ by IQLearning LLC: planners and resources for graduate students.",'''<div class="hero"><div class="wrap"><p class="eyebrow">Grad-IQ by IQLearning LLC · Las Vegas, NV</p>
<h1>Planners and resources built for graduate students</h1><p class="lede">Grad-IQ serves grad students everywhere, including across the whole University of California system, with practical planners for money, study and the PhD journey.</p>
<div class="btns"><a class="btn primary" href="planners.html">Browse planners</a><a class="btn" href="save-checklist.html">Free SAVE checklist</a></div></div></div>
<section><div class="wrap"><h2>Explore Grad-IQ</h2><div class="grid">
<a class="card tint4" href="planners.html" style="text-decoration:none;color:inherit"><h3>Planners</h3><p>Five browser-based planners for budgets, health costs, study and your PhD roadmap. Try every demo free.</p></a>
<a class="card tint3" href="regalia.html" style="text-decoration:none;color:inherit"><h3>Ph.D. Regalia</h3><p>Buy once-used doctoral regalia for less than retail, or sell your set to Grad-IQ.</p></a>
<a class="card tint1" href="save-checklist.html" style="text-decoration:none;color:inherit"><h3>Free SAVE Plan Exit Checklist</h3><p>A free step-by-step checklist for borrowers leaving the SAVE repayment plan.</p></a>
<a class="card tint2" href="app.html" style="text-decoration:none;color:inherit"><h3>Grad-IQ Planners app</h3><p>Planners on your phone, coming soon to the App Store and Google Play.</p></a>
</div></div></section>''')
pages["planners.html"]=("Planners","Grad-IQ planners for graduate students, $19 each.",f'''<div class="hero"><div class="wrap"><p class="eyebrow">Planners</p><h1>Grad-IQ planners</h1><p class="lede">Each demo runs in your browser with sample data, so you can try it before you buy. The full edition saves in your browser and adds backup, CSV export and print.</p></div></div>
<section><div class="wrap"><div class="grid">{cards}</div><p class="note">Full editions will be sold through Etsy. Listings are coming soon.</p></div></section>''')
pages["regalia.html"]=("Ph.D. Regalia","Buy once-used Ph.D. regalia or sell yours to Grad-IQ.",'''<div class="hero"><div class="wrap"><p class="eyebrow">Ph.D. Regalia</p><h1>Doctoral regalia, worn once</h1><p class="lede">Doctoral regalia is usually worn for a single ceremony. Grad-IQ buys used sets from new graduates and resells them to the next class for less than retail.</p></div></div>
<section><div class="wrap"><div class="grid">
<div class="card tint4"><h3>Buy once-used regalia</h3><p>Get a complete used Ph.D. regalia set for less than buying new.</p><p class="price">$250–$300</p><p class="note">Typical resale price for a full set. Availability varies; email us with your institution and size.</p><div class="spacer"></div><a class="btn primary" href="mailto:jay.s@grad-iq.org?subject=Buying%20Ph.D.%20regalia">Ask about available sets</a></div>
<div class="card tint1"><h3>Sell yours to Grad-IQ</h3><p>Done with your regalia after commencement? Sell it to us instead of letting it sit in a closet.</p><p class="price">$125</p><p class="note">For a full used set. Email us with your institution and the items you have.</p><div class="spacer"></div><a class="btn primary" href="mailto:jay.s@grad-iq.org?subject=Selling%20my%20Ph.D.%20regalia">Sell your regalia</a></div>
</div></div></section>''')
pages["save-checklist.html"]=("Free SAVE Plan Exit Checklist","A free checklist for federal student-loan borrowers leaving the SAVE plan.",'''<div class="hero"><div class="wrap split"><div><p class="eyebrow">Free resource</p><h1>SAVE Plan Exit Checklist</h1><p class="lede">If you're a federal student-loan borrower moving off the SAVE plan, this free checklist walks you through it step by step: your servicer notices and deadlines, the repayment plans you can choose, what happens if you don't choose, and what it means for PSLF.</p>
<div class="btns"><a class="btn primary" href="https://gradiq.github.io/save-plan-exit-checklist/" target="_blank" rel="noopener">Open the free checklist</a></div><p class="note">Free, runs in your browser. It's a planning aid, not legal or financial advice; your loan servicer sets final terms.</p></div>
<img class="shot" style="max-width:320px;justify-self:center" src="assets/img/save-exit.png" alt="SAVE Plan Exit Checklist on a phone"></div></div>''')
pages["app.html"]=("App","Grad-IQ Planners app for iPhone, iPad and Android.",'''<div class="hero"><div class="wrap split"><div><p class="eyebrow">Mobile app</p><h1>Grad-IQ Planners app</h1><p class="lede">Four offline planners in one app: PhD Stipend &amp; Loan Budget, Burnout-Proof Study Tracker, PhD Roadmap, and Lumen 7-Step Planner.</p>
<p><span class="tag">Coming soon to the App Store and Google Play</span></p><div class="btns"><a class="btn primary" href="https://gradiq.github.io/grad-iq-app-preview/" target="_blank" rel="noopener">See the app preview</a></div></div>
<img class="shot" style="max-width:300px;justify-self:center" src="assets/img/app.png" alt="Grad-IQ Planners app home screen"></div></div>
<section><div class="wrap"><div class="grid"><div class="card"><h3>Free download</h3><p>Try every planner with sample data. Fully usable, but nothing is saved and there's no backup or export.</p></div>
<div class="card tint4"><h3>$19.99 one-time unlock</h3><p>Saves your entries on the device, adds backup and restore, CSV export, and loan due-date reminders. No subscription.</p></div>
<div class="card tint1"><h3>Private by design</h3><p>Your data stays on your device. No account or login. Read the <a href="privacy.html">privacy policy</a>.</p></div></div></div></section>''')
pages["privacy.html"]=("Privacy Policy","Grad-IQ Planners privacy policy, IQLearning LLC.",'<div class="hero"><div class="wrap"><p class="eyebrow">Grad-IQ by IQLearning LLC</p><h1>Privacy Policy</h1><p class="lede">Grad-IQ Planners app</p></div></div><section><div class="wrap prose">'+open('/tmp/priv.html').read()+'</div></section>')
pages["about.html"]=("About","About Grad-IQ and IQ Learning.",'''<div class="hero"><div class="wrap"><p class="eyebrow">About</p><h1>About Grad-IQ</h1><p class="lede">Grad-IQ is a brand of IQ Learning (IQLearning LLC), based in Las Vegas, Nevada. We make practical tools for graduate students.</p></div></div>
<section><div class="wrap grid"><div class="card tint4"><h3>IQ Learning</h3><p>IQ Learning is Grad-IQ's parent company.</p></div>
<div class="card tint3"><h3>Sister brand: TrivQ</h3><p>TrivQ makes educational board games, starting with TrivQ Judaica.</p><div class="spacer"></div><a class="btn" href="https://trivq.org" target="_blank" rel="noopener">Visit trivq.org</a></div>
<div class="card tint1"><h3>Who we are</h3><p>Grad-IQ is managed by Dr. Evelyn &ldquo;Evy&rdquo; Mayes and Jay S., Director of Operations.</p></div></div></section>''')
pages["contact.html"]=("Contact","Contact Grad-IQ.",'''<div class="hero"><div class="wrap"><p class="eyebrow">Contact</p><h1>Get in touch</h1><p class="lede">Questions about planners, regalia or the app? Email us and we'll reply.</p></div></div>
<section><div class="wrap grid"><div class="card"><h3>Email</h3><p><a href="mailto:jay.s@grad-iq.org">jay.s@grad-iq.org</a></p><a class="btn primary" href="mailto:jay.s@grad-iq.org">Email Grad-IQ</a></div>
<div class="card tint2"><h3>Location</h3><p>IQLearning LLC<br>Las Vegas, NV</p></div></div></section>''')
for fn,(t,d,b) in pages.items(): open(fn,'w').write(page(fn,t,d,b))
