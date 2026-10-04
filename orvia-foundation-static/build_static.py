from pathlib import Path
import html, shutil

ROOT = Path('/mnt/data/orvia-foundation-static')
BASE_URL = 'https://foundation.orvia.org.uk'

# Remove generated route folders from the previous, fuller launch concept.
for d in ['access','apply','community','governance','impact','learning','partners','veterans','about','privacy','terms','accessibility','cookies','resources']:
    p = ROOT/d
    if p.exists():
        shutil.rmtree(p)

LOCAL_NAV = [
    ('/','Foundation'),
    ('/veterans/','Veterans & Families'),
    ('/resources/','Free Resources'),
    ('/about/','About')
]

ORVIA_PRIMARY = [
    ('https://orvia.org.uk/about','About'),
    ('https://orvia.org.uk/services','What We Do'),
    ('https://orvia.org.uk/method','Method'),
    ('https://orvia.org.uk/blog','Blog'),
    ('https://orvia.org.uk/trust','Trust'),
    ('https://orvia.org.uk/contact','Contact')
]

HEADER = '''
<div class="estate-bar"><div class="shell estate-inner">
  <a class="estate-home" href="https://orvia.org.uk"><strong>ORVIA OVERSIGHT</strong><span>Human first. Human last.</span></a>
  <div class="estate-links"><span>Part of the ORVIA estate</span><a href="https://orvia.org.uk/trust">Trust Centre</a><a href="https://orvia.org.uk/contact">Contact ORVIA</a></div>
</div></div>
<header class="orvia-header"><div class="shell orvia-header-inner">
  <a href="https://orvia.org.uk" class="master-brand" aria-label="ORVIA Oversight home"><img src="https://orvia.org.uk/brand/ORVIA-Oversight-master.png" alt="ORVIA Oversight"></a>
  <nav class="orvia-main-nav" aria-label="ORVIA main navigation">{orvia_nav}</nav>
  <div class="orvia-header-actions"><a class="customer-link" href="https://workspace.orvia.org.uk">Customer login</a><a class="button button-primary compact" href="https://orvia.org.uk/contact">Tell Us What's Happening</a></div>
</div></header>
<div class="foundation-nav"><div class="shell foundation-nav-inner">
  <a class="foundation-brand" href="/"><span class="foundation-mark">F</span><span><strong>ORVIA FOUNDATION</strong><small>IN DEVELOPMENT</small></span></a>
  <nav class="foundation-links" aria-label="Foundation navigation">{local_nav}</nav>
  <details class="mobile-menu"><summary>Menu</summary><div class="mobile-panel">{mobile_nav}</div></details>
</div></div>
'''

FOOTER = '''
<footer class="footer"><div class="shell">
  <div class="footer-main">
    <div class="footer-brand">
      <a href="https://orvia.org.uk"><img src="https://orvia.org.uk/brand/ORVIA-Oversight-master.png" alt="ORVIA Oversight"></a>
      <p><strong>Observation · Reflection · Visibility · Insight · Accountability</strong><br>Human first. Human last. Truth before comfort.</p>
      <p><a href="tel:+443300433703">0330 043 3703</a><br><a href="mailto:hello@orvia.org.uk">hello@orvia.org.uk</a></p>
    </div>
    <div class="footer-col"><h3>START HERE</h3>
      <a href="https://orvia.org.uk/resources">Free Resources</a><a href="https://orvia.org.uk/work-with-orvia">Work with ORVIA</a><a href="https://orvia.org.uk/products">Products</a><a href="https://workspace.orvia.org.uk">Customer Access</a><a href="https://orvia.org.uk/contact">Contact</a>
    </div>
    <div class="footer-col"><h3>METHOD + PRODUCTS</h3>
      <a href="https://orvia.org.uk/method">ORVIA Method</a><a href="https://orvia.org.uk/services">Service Information</a><a href="https://orviavoice.co.uk">ORVIA Voice</a><a href="https://witness.orvia.org.uk">Witness Room</a><a href="https://threshold.orvia.org.uk">Threshold</a>
    </div>
    <div class="footer-col"><h3>COMPANY</h3>
      <a href="https://orvia.org.uk/about">About ORVIA</a><a href="https://orvia.org.uk/founder">Founder Story</a><a href="https://orvia.org.uk/armed-forces">Armed Forces</a><a href="https://orvia.org.uk/careers">Careers</a><a href="https://orvia.org.uk/trust">Trust Centre</a><a href="https://www.trustaveteran.com/team/orvia">Trust A Veteran</a>
    </div>
    <div class="footer-signature"><strong>Human first.<br>Human last.<br>Truth before comfort.</strong><span></span></div>
  </div>
  <div class="footer-trust"><strong>Verified trust:</strong><a href="https://www.armedforcescovenant.gov.uk/">Armed Forces Covenant</a><a href="https://orvia.org.uk/trust">Companies House 16123685</a><a href="https://orvia.org.uk/trust">ICO ZC152311</a><a href="https://orvia.org.uk/armed-forces">ERS Bronze</a><a href="https://orvia.org.uk/founder">Veteran-founded</a><a href="https://www.trustaveteran.com/team/orvia">Trust A Veteran</a></div>
  <div class="foundation-disclosure"><strong>ORVIA Foundation</strong><span>A public-benefit programme being developed by ORVIA Oversight Ltd. It is not presented as a registered charity and is not currently accepting public donations or open grant applications.</span></div>
  <div class="footer-bottom"><div><span>© 2026 ORVIA Oversight Ltd</span><span>Company 16123685</span><span>ICO ZC152311</span><a href="https://orviaweb.co.uk">Built by ORVIA Web</a></div><div><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/cookies/">Cookies</a><a href="/accessibility/">Accessibility</a></div></div>
</div></footer>
'''


def wrapper(title, body, desc='ORVIA Foundation'):
    orvia_nav=''.join(f'<a href="{h}">{html.escape(l)}</a>' for h,l in ORVIA_PRIMARY)
    local_nav=''.join(f'<a href="{h}">{html.escape(l)}</a>' for h,l in LOCAL_NAV)
    mobile_nav=local_nav + '<hr><a href="https://orvia.org.uk">ORVIA Oversight</a><a href="https://orvia.org.uk/trust">Trust Centre</a><a href="https://orvia.org.uk/contact">Contact ORVIA</a>'
    header = HEADER.format(orvia_nav=orvia_nav, local_nav=local_nav, mobile_nav=mobile_nav)
    canonical = BASE_URL + ('/' if title == 'ORVIA Foundation' else '')
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | ORVIA Foundation</title><meta name="description" content="{html.escape(desc)}"><meta name="theme-color" content="#0A2342"><link rel="canonical" href="{canonical}"><link rel="stylesheet" href="/styles.css"></head><body>{header}<main>{body}</main>{FOOTER}</body></html>'''


def write_page(path, title, body, desc='ORVIA Foundation'):
    p=ROOT/path
    p.mkdir(parents=True, exist_ok=True)
    (p/'index.html').write_text(wrapper(title,body,desc),encoding='utf-8')

home='''
<section class="hero"><div class="shell hero-grid">
  <div class="hero-copy"><span class="status-pill">IN DEVELOPMENT</span><span class="eyebrow">ORVIA FOUNDATION</span><h1>Capability should create <em>opportunity.</em></h1><p>We are building a practical public-benefit route around access, learning, veterans and opportunity — carefully, and without pretending the programmes are further advanced than they are.</p><div class="actions"><a class="button button-primary" href="/resources/">Explore free resources</a><a class="button button-secondary" href="https://orvia.org.uk/contact">Contact ORVIA</a></div><div class="trust-row"><span>Part of ORVIA Oversight</span><span>Veteran-founded</span><span>Human decisions</span></div></div>
  <div class="hero-media"><figure class="hero-main"><img src="https://orvia.org.uk/images/golden-master/people/orvia-people-03.png" alt="People from different life experiences in a supportive conversation"></figure><figure><img src="https://orvia.org.uk/images/golden-master/people/orvia-people-06.png" alt="People working together in a practical setting"></figure><div class="media-card"><span>FOUNDATION STATUS</span><strong>Building the first routes properly before opening them widely.</strong></div></div>
</div></section>

<section class="foundation-status"><div class="shell status-grid"><div><span class="eyebrow light">WORK IN PROGRESS</span><h2>The purpose is clear. The operating model is still being built.</h2></div><div><p>Foundation exists to open doors when cost, circumstance or an unconventional path would otherwise close them. For now, we are keeping the public promise deliberately small.</p><ul class="check-list"><li>Free resources can be used now</li><li>Veteran and Service-family pathways are being developed</li><li>Wider supported-access programmes are not yet open</li><li>No public donations or grant applications at this stage</li></ul></div></div></section>

<section class="section"><div class="shell"><div class="section-head"><span class="eyebrow">WHAT FOUNDATION WILL FOCUS ON</span><h2>Four simple areas.</h2><p>Enough to explain the direction without presenting future ideas as established programmes.</p></div><div class="pillar-grid"><article class="pillar navy"><span>01</span><h3>Access</h3><p>Remove cost barriers where an appropriate ORVIA route can genuinely help.</p></article><article class="pillar teal"><span>02</span><h3>Opportunity</h3><p>Create credible routes for veterans, Service families and people with unconventional experience.</p></article><article class="pillar gold"><span>03</span><h3>Learning</h3><p>Make useful tools and introductory knowledge available before somebody has to buy anything.</p></article><article class="pillar purple"><span>04</span><h3>Community</h3><p>Support practical projects closely aligned to ORVIA's purpose as capacity develops.</p></article></div></div></section>

<section class="section section-soft"><div class="shell live-grid"><div><span class="eyebrow">AVAILABLE NOW</span><h2>Start with what is real.</h2><p>The Open Toolkit is live. It contains simple resources for evidence, chronology and skills translation, with no email gate for basic downloads.</p><a class="button button-primary" href="/resources/">Open the free toolkit</a></div><div class="live-card"><span class="live-dot"></span><strong>Open Toolkit</strong><p>Free downloadable resources.</p><span class="live-label">LIVE</span></div><div class="live-card"><span class="develop-dot"></span><strong>Veterans & Families</strong><p>Pathways and support model in development.</p><span class="develop-label">DEVELOPING</span></div></div></section>

<section class="section"><div class="shell split"><div><span class="eyebrow">VETERANS & SERVICE FAMILIES</span><h2>Make the Covenant mean something practical.</h2><p>ORVIA is veteran-founded, an Armed Forces Covenant signatory and an ERS Bronze Award holder. Foundation will turn that commitment into practical opportunity as the pathway develops.</p><a class="button button-secondary" href="/veterans/">Read the current direction</a></div><figure class="round-image"><img src="https://orvia.org.uk/images/golden-master/people/orvia-people-10.png" alt="People and professionals together in a supportive setting"></figure></div></section>

<section class="final"><div class="shell final-inner"><div><span class="eyebrow light">ORVIA FOUNDATION</span><h2>Open doors carefully. Build the support properly.</h2><p>For Foundation enquiries while the programme is developing, contact ORVIA Oversight.</p></div><div class="actions"><a class="button button-gold" href="https://orvia.org.uk/contact">Contact ORVIA</a><a class="button button-white" href="/about/">About Foundation</a></div></div></section>
'''
(ROOT/'index.html').write_text(wrapper('ORVIA Foundation',home,'ORVIA Foundation is an in-development public-benefit programme focused on access, opportunity, learning and community.'),encoding='utf-8')

veterans='''
<section class="page-hero"><div class="shell narrow"><span class="status-pill">DEVELOPING</span><span class="eyebrow">VETERANS & SERVICE FAMILIES</span><h1>Turn Service experience into practical opportunity.</h1><p>The pathway is still being developed. The intention is to translate real experience into civilian capability without exaggeration, and to recognise the wider impact of Service life on families.</p></div></section>
<section class="section"><div class="shell three-grid"><article class="content-card"><span>01</span><h2>Skills translation</h2><p>Help people describe what they can actually do in language civilian employers and organisations understand.</p></article><article class="content-card"><span>02</span><h2>Mentoring + learning</h2><p>Build practical guidance, learning routes and future Academy links where they add real value.</p></article><article class="content-card"><span>03</span><h2>Service families</h2><p>Keep spouses, partners, Reservists and people returning after disruption within the future pathway.</p></article></div><div class="simple-note"><strong>Current position</strong><p>This is not an open employment or bursary scheme yet. The first public resource available now is the Veteran Skills Translation Guide.</p><a class="button button-primary" href="/resources/">Open the guide</a></div></div></section>
'''
write_page('veterans','Veterans & Service Families',veterans,'The developing ORVIA Foundation pathway for veterans, Service leavers, Reservists and Service families.')

resources=[
('Concern clarity checklist','Separate the concern, what is known, what is assumed and what needs checking.','/resources/concern-clarity-checklist.txt'),
('Chronology template','A simple structure for dates, source, event, disputed points and what remains unknown.','/resources/chronology-template.txt'),
('Evidence language worksheet','Work in fact · account · interpretation · assumption · unknown.','/resources/evidence-language-worksheet.txt'),
('Veteran skills translation guide','Turn Service experience into civilian capability language without exaggeration.','/resources/veteran-skills-translation-guide.txt')]
cards=''.join(f'<article class="resource-card"><span>FREE RESOURCE</span><h2>{html.escape(t)}</h2><p>{html.escape(d)}</p><a class="button button-secondary" href="{h}" download>Download</a></article>' for t,d,h in resources)
write_page('resources','Free Resources',f'<section class="page-hero"><div class="shell narrow"><span class="status-pill live">LIVE</span><span class="eyebrow">OPEN TOOLKIT</span><h1>Useful before you buy anything.</h1><p>These are simple launch resources. No email gate and no claim that the wider Foundation programme is already open.</p></div></section><section class="section"><div class="shell resource-grid">{cards}</div></section>','Free ORVIA Foundation tools for evidence, chronology and veteran skills translation.')

about='''
<section class="page-hero"><div class="shell narrow"><span class="eyebrow">ABOUT</span><h1>Foundation exists to open doors.</h1><p>The idea is simple: commercial capability should create public value. ORVIA Foundation is being developed as the place where ORVIA can widen access to useful help, learning and opportunity.</p></div></section>
<section class="section"><div class="shell two-grid"><article class="content-card"><span>01</span><h2>Why it exists</h2><p>Help should not disappear purely because somebody cannot afford the commercial route. Experience should not be wasted because it does not fit a conventional CV.</p></article><article class="content-card"><span>02</span><h2>What it is today</h2><p>A public-benefit programme being developed by ORVIA Oversight Ltd. It is not presented as a registered charity and broader funding/support routes are not yet open.</p></article></div><div class="quote-card wide"><strong>Foundation opens the door.</strong><span>Academy builds the capability.</span></div></div></section>
'''
write_page('about','About ORVIA Foundation',about,'Why ORVIA Foundation exists and its current in-development status.')

legal_pages = {
'privacy':('PRIVACY','Keep data collection proportionate.','Foundation is still developing, so this site deliberately avoids a detailed support application. Do not send medical records, legal evidence, safeguarding documents, financial statements or other highly sensitive material by ordinary email. For general Foundation enquiries use the main ORVIA contact route.'),
'terms':('TERMS','Clear boundaries while Foundation develops.','ORVIA Foundation is not an emergency service, crisis line, safeguarding authority, law firm, financial adviser or clinical provider. The site describes an in-development public-benefit programme and does not offer or guarantee grants, bursaries, employment or funded services.'),
'accessibility':('ACCESSIBILITY','The route to help should not be a maze.','Foundation aims to follow the wider ORVIA accessibility standard: plain English, strong contrast, readable layouts, keyboard access and practical alternatives where a digital route creates a barrier.'),
'cookies':('COOKIES','Keep tracking restrained.','Foundation should use only the cookies and measurement needed to operate and improve the site, following the wider ORVIA consent standard. Vulnerability or hardship information must not be used for advertising or retargeting.')
}
for slug,(eyebrow,title,intro) in legal_pages.items():
    body=f'<section class="page-hero legal"><div class="shell narrow"><span class="eyebrow">{eyebrow}</span><h1>{html.escape(title)}</h1><p>{html.escape(intro)}</p><div class="actions"><a class="button button-secondary" href="https://orvia.org.uk/trust">ORVIA Trust Centre</a><a class="button button-primary" href="https://orvia.org.uk/contact">Contact ORVIA</a></div></div></section>'
    write_page(slug,title,body,intro)

(ROOT/'404.html').write_text(wrapper('Page not found','<section class="page-hero"><div class="shell narrow"><span class="eyebrow">404</span><h1>That page is not here.</h1><p>Foundation is being simplified while it is developed. Return to the current public site.</p><div class="actions"><a class="button button-primary" href="/">Foundation home</a></div></div></section>'),encoding='utf-8')

# Redirect old concept routes back to the reduced public surface.
redirects = [
    {"source":"/access/:path*","destination":"/","permanent":False},
    {"source":"/apply/:path*","destination":"/","permanent":False},
    {"source":"/community/:path*","destination":"/","permanent":False},
    {"source":"/governance/:path*","destination":"/about/","permanent":False},
    {"source":"/impact/:path*","destination":"/about/","permanent":False},
    {"source":"/learning/:path*","destination":"/resources/","permanent":False},
    {"source":"/partners/:path*","destination":"/","permanent":False}
]
import json
(ROOT/'vercel.json').write_text(json.dumps({"cleanUrls":True,"trailingSlash":True,"redirects":redirects},indent=2),encoding='utf-8')
(ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n',encoding='utf-8')
urls=['','veterans','resources','about','privacy','terms','accessibility','cookies']
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{BASE_URL}/{u+"/" if u else ""}</loc></url>\n' for u in urls)+'</urlset>',encoding='utf-8')
print('built',len(urls),'public routes')
