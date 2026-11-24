#!/usr/bin/env python3
"""Static site generator for baez.studio.

Writes plain HTML pages (everything server-rendered, no JS needed to read
copy, pricing, FAQ or JSON-LD) into the repo root, ready for GitHub Pages.

  python3 _build/build.py            # production build into repo root
  python3 _build/build.py --preview  DIR   # same site with index.html links, for file/preview hosting

Links inside page bodies use tokens:
  [[L:video-production/]]   -> relative link to a page
  [[A:assets/css/site.css]] -> relative link to a file
"""
import json, os, re, sys, html

sys.path.insert(0, os.path.dirname(__file__))
from content import PAGES, SITE  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PREVIEW = '--preview' in sys.argv
OUT = sys.argv[sys.argv.index('--preview') + 1] if PREVIEW else ROOT


def rel(from_path, to, is_page):
    """Relative URL from page `from_path` ('' or 'work/x/') to target."""
    depth = from_path.count('/')
    prefix = '../' * depth
    frag = ''
    if '#' in to:
        to, frag = to.split('#', 1)
        frag = '#' + frag
    if is_page:
        if to == '' and frag and from_path == '':
            return frag
        target = to
        if PREVIEW:
            target = to + 'index.html'
        url = prefix + target
        if url == '':
            url = './'
        return url + frag
    return prefix + to + frag


def render_tokens(body, path):
    body = re.sub(r'\[\[L:([^\]]*)\]\]', lambda m: rel(path, m.group(1), True), body)
    body = re.sub(r'\[\[A:([^\]]*)\]\]', lambda m: rel(path, m.group(1), False), body)
    return body


NAV = [
    ('video-production/', 'Video Production'),
    ('ai-business-stacks/', 'AI Business Stacks'),
    ('work/', 'Work'),
    ('#process', 'Process'),
    ('#pricing', 'Pricing'),
    ('about/', 'About'),
]


def header(path):
    items = []
    for href, label in NAV:
        if href.startswith('#'):
            link = '[[L:' + href + ']]'
        else:
            link = '[[L:' + href + ']]'
        cur = ' aria-current="page"' if (not href.startswith('#') and path.startswith(href)) else ''
        items.append('<li><a href="%s"%s>%s</a></li>' % (link, cur, label))
    items.append('<li class="mobile-only"><a href="mailto:%s">%s</a></li>' % (SITE['email'], SITE['email']))
    return '''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="wrap nav" aria-label="Primary">
    <a class="wordmark" href="[[L:]]" aria-label="Baez Studio home">BAEZ<span>.</span>AI<span>.</span>STUDIO</a>
    <ul class="nav-links" id="nav-links">%s</ul>
    <div class="nav-cta">
      <a class="nav-mail" href="mailto:%s">%s</a>
      <a class="btn btn-primary btn-sm" href="[[L:book/]]">Book a Call</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
    </div>
  </nav>
</header>''' % (''.join(items), SITE['email'], SITE['email'])


def footer():
    s = SITE
    return '''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="wordmark" href="[[L:]]">BAEZ<span>.</span>AI<span>.</span>STUDIO</a>
        <p class="mt2">Cinematic AI video and custom AI business stacks, directed by Josh Baez. 15+ years of commercial post-production. Ann Arbor, MI · Fort Wayne, IN · Worldwide.</p>
        <p><a class="mail" href="mailto:%(email)s">%(email)s</a></p>
      </div>
      <div>
        <h2>Services</h2>
        <ul>
          <li><a href="[[L:video-production/]]">Cinematic AI Video</a></li>
          <li><a href="[[L:ai-business-stacks/]]">AI Business Stacks</a></li>
          <li><a href="[[L:#pricing]]">Pricing</a></li>
          <li><a href="[[L:work/]]">Work</a></li>
        </ul>
      </div>
      <div>
        <h2>Studio</h2>
        <ul>
          <li><a href="[[L:about/]]">About Josh</a></li>
          <li><a href="[[L:locations/]]">Service Areas</a></li>
          <li><a href="[[L:locations/ann-arbor/]]">Ann Arbor, MI</a></li>
          <li><a href="[[L:locations/fort-wayne/]]">Fort Wayne, IN</a></li>
          <li><a href="[[L:book/]]">Book a Call</a></li>
        </ul>
      </div>
      <div>
        <h2>Follow</h2>
        <ul>
          <li><a href="%(linkedin)s" rel="me noopener" target="_blank">LinkedIn</a></li>
          <li><a href="%(instagram)s" rel="me noopener" target="_blank">Instagram</a></li>
          <li><a href="%(x)s" rel="me noopener" target="_blank">X / Twitter</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© 2026 Baez Studio (BAEZ.AI.STUDIO). All rights reserved.</span>
      <span>Service-area studio · no public office address · remote-first worldwide</span>
    </div>
  </div>
</footer>''' % s


REEL_DIALOG = '''<dialog class="reel" id="reel" aria-label="Showreel" data-embed="https://player.vimeo.com/video/%s?title=0&byline=0&portrait=0&dnt=1">
  <div class="bar"><span class="mono">Baez Studio · Showreel</span><button class="btn btn-ghost btn-sm" type="button" data-close>Close</button></div>
  <div class="ratio"></div>
</dialog>'''


def org_ld():
    s = SITE
    url = s['url']
    founder = {
        "@type": "Person", "@id": url + "#josh", "name": "Josh Baez",
        "jobTitle": "Founder & Creative Director", "url": url + "about/",
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Point Park University"},
        "sameAs": [s['linkedin'], s['instagram'], s['x']],
    }
    catalog = {
        "@type": "OfferCatalog", "name": "Baez Studio services",
        "itemListElement": [
            {"@type": "OfferCatalog", "name": "Cinematic AI Video Production", "itemListElement": [
                offer("Single Shot", 1500, None, "USD"), offer("Hook Pack", 2500, None, "USD"),
                offer("Signature Brand Film", 5000, None, "USD"), offer("Cinematic Video Retainer", 7500, None, "USD", "MON")]},
            {"@type": "OfferCatalog", "name": "Custom AI Business Stacks", "itemListElement": [
                offer("AI Workflow Audit & Blueprint", 750, 1500, "USD"), offer("Starter AI Business Stack", 2500, 6500, "USD"),
                offer("Growth AI Operations Stack", 7500, 18000, "USD"), offer("Stack Care & Optimization Plan", 500, 1500, "USD", "MON"),
                offer("Hybrid Growth Retainer", 4500, 9500, "USD", "MON")]},
        ]}
    return [{
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": url + "#studio",
        "name": "Baez Studio", "alternateName": "BAEZ.AI.STUDIO", "url": url, "email": s['email'],
        "logo": url + "og-card.png", "image": url + "og-card.png",
        "description": "Boutique studio pairing 15+ years of commercial editing with generative AI compositing, Remotion programmatic video and bespoke AI business workflows.",
        "founder": founder, "priceRange": "$750 – $18,000",
        "areaServed": [
            {"@type": "City", "name": "Ann Arbor", "containedInPlace": {"@type": "State", "name": "Michigan"}},
            {"@type": "City", "name": "Fort Wayne", "containedInPlace": {"@type": "State", "name": "Indiana"}},
            {"@type": "Country", "name": "United States"}, "Worldwide"],
        "knowsAbout": ["AI video production", "Generative AI compositing", "Remotion", "Paid social creative", "AI workflow automation", "n8n", "Make", "Google Workspace automation"],
        "sameAs": [s['linkedin'], s['instagram'], s['x']],
        "hasOfferCatalog": catalog,
    }, {
        "@context": "https://schema.org", "@type": "WebSite", "@id": url + "#website", "name": "Baez Studio",
        "alternateName": "BAEZ.AI.STUDIO", "url": url, "publisher": {"@id": url + "#studio"}, "inLanguage": "en-US",
    }]


def offer(name, lo, hi, cur, unit=None):
    ps = {"@type": "PriceSpecification" if not unit else "UnitPriceSpecification", "priceCurrency": cur}
    if hi:
        ps["minPrice"] = lo
        ps["maxPrice"] = hi
    else:
        ps["minPrice"] = lo
    if unit:
        ps["unitCode"] = unit
    return {"@type": "Offer", "itemOffered": {"@type": "Service", "name": name}, "priceSpecification": ps}


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}} for q, a in faqs]}


def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE['url'] + p} for i, (n, p) in enumerate(trail)]}


def ld_block(obj):
    # Plain UTF-8 JSON; only "</" is escaped so the block can't close early. No HTML entities.
    txt = json.dumps(obj, ensure_ascii=False, indent=1).replace('</', '<\\/')
    return '<script type="application/ld+json">\n' + txt + '\n</script>'


def faq_html(faqs, heading_level='h3'):
    out = ['<div class="faq">']
    for q, a in faqs:
        out.append('<details><summary><%s>%s</%s></summary><div class="answer"><p>%s</p></div></details>' % (heading_level, q, heading_level, a))
    out.append('</div>')
    return '\n'.join(out)


def page(p):
    path = p['path']
    url = SITE['url'] + path
    lds = []
    if p.get('org', True):
        lds += org_ld()
    lds += p.get('ld', [])
    if p.get('faqs'):
        lds.append(faq_ld(p['faqs']))
    if p.get('crumbs'):
        lds.append(crumbs_ld(p['crumbs']))
    body = p['body']
    if p.get('faqs'):
        body = body.replace('[[FAQ]]', faq_html(p['faqs']))
    preload = p.get('preload', '')
    doc = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta name="robots" content="%(robots)s">
<meta name="theme-color" content="#0A0A0C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Baez Studio">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(site)sog-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@baezaistudio">
<meta name="twitter:image" content="%(site)sog-card.png">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%%3E%%3Crect width='64' height='64' rx='14' fill='%%230A0A0C'/%%3E%%3Ctext x='32' y='45' font-family='Georgia,serif' font-size='40' text-anchor='middle' fill='%%23F5B841'%%3EB%%3C/text%%3E%%3C/svg%%3E">
%(preload)s
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="[[A:assets/css/site.css]]?v=%(ver)s">
<script async src="https://www.googletagmanager.com/gtag/js?id=%(ga)s"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','%(ga)s');</script>
%(ld)s
</head>
<body>
%(header)s
<main id="main">
%(body)s
</main>
%(footer)s
%(dialog)s
<script src="[[A:assets/js/site.js]]?v=%(ver)s" defer></script>
</body>
</html>
''' % {
        'title': html.escape(p['title']), 'desc': html.escape(p['desc']), 'url': url, 'site': SITE['url'],
        'preload': preload, 'robots': 'noindex' if p.get('noindex') else 'index,follow,max-image-preview:large,max-video-preview:-1', 'ga': SITE['ga'], 'ver': SITE['ver'],
        'ld': '\n'.join(ld_block(x) for x in lds), 'header': header(path), 'body': body,
        'footer': footer(), 'dialog': REEL_DIALOG % SITE['vimeo'] if p.get('reel') else '',
    }
    return render_tokens(doc, path)


def main():
    for p in PAGES:
        dest = os.path.join(OUT, p['path'], 'index.html') if p['path'] != '404' else os.path.join(OUT, '404.html')
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if p['path'] == '404':
            p = dict(p, path='')  # 404 is served at any depth: use absolute links
            doc = page(p)
            doc = re.sub(r'(href|src)="(?!https?:|mailto:|#|data:)\.?/?([^"]*)"', lambda m: '%s="/%s"' % (m.group(1), m.group(2)), doc)
        else:
            doc = page(p)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(doc)
    if not PREVIEW:
        write_seo()
    print('built %d pages -> %s' % (len(PAGES), OUT))


def write_seo():
    urls = [p for p in PAGES if p['path'] != '404']
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        sm.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (
            SITE['url'], p['path'], SITE['modified'], p.get('priority', '0.7')))
    sm.append('</urlset>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')


if __name__ == '__main__':
    main()
