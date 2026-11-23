"""All copy for baez.studio lives here. Edit text, rebuild with `python3 _build/build.py`."""

SITE = {
    'url': 'https://baez.studio/',
    'email': 'josh@baez.studio',
    'linkedin': 'https://www.linkedin.com/in/josh-baez-1bab4430a',
    'instagram': 'https://www.instagram.com/baez.ai.studio/',
    'x': 'https://x.com/baezaistudio',
    'cal': 'baezstudio/15min',
    'formspree': 'https://formspree.io/f/xnjrdwyv',
    'vimeo': '1194564875',
    'ga': 'G-LPQ3NP81MN',
    'modified': '2026-11-23',
    'updated_label': 'November 2026',
    'ver': '20261123',
}

UPDATED = '<p class="updated">Last updated: %s</p>' % SITE['updated_label']

# ---------------------------------------------------------------- shared blocks

PILLARS = '''<div class="grid g2">
  <a class="card pillar" href="[[L:video-production/]]">
    <span class="eyebrow cinema">Pillar 01 · Cinematic AI Video &amp; Paid Social</span>
    <h3>Films that stop the scroll, cut by an editor who has done it for 15 years.</h3>
    <p>Brand films, brand revivals, lore and game cinematics, and performance hook packs for Meta, TikTok and YouTube. Generative compositing directed shot by shot, finished in a real NLE.</p>
    <div class="tags"><span class="tag cinema">Brand Films</span><span class="tag cinema">Hook Packs</span><span class="tag cinema">Lore &amp; Worlds</span><span class="tag cinema">Remotion Variants</span></div>
    <span class="link-arrow">Explore Video Packages</span>
  </a>
  <a class="card pillar systems" href="[[L:ai-business-stacks/]]">
    <span class="eyebrow systems">Pillar 02 · Custom AI Business Stacks</span>
    <h3>One spreadsheet in, a week of emails, flyers and posts out.</h3>
    <p>Bespoke ChatGPT, Gemini and Claude workflows wired to your Sheets, CRM and inbox. Automated spreadsheets, lifecycle emails, newsletters, branded flyers and social content engines that your team owns outright.</p>
    <div class="tags"><span class="tag systems">Automated Sheets</span><span class="tag systems">Lifecycle Email</span><span class="tag systems">Newsletters</span><span class="tag systems">Flyer &amp; Social Engines</span></div>
    <span class="link-arrow">Explore AI Stacks</span>
  </a>
</div>'''

VIDEO_PRICES = '''<div class="price-grid">
  <article class="card price">
    <h3>Single Shot</h3>
    <p class="amt">From $1,500<small>per project</small></p>
    <p class="time">5–7 business days</p>
    <ul><li>1× polished video up to 30s</li><li>Original music &amp; sound design</li><li>2 revision rounds</li><li>4K master + 9:16 / 1:1 / 16:9 exports</li></ul>
    <a class="btn btn-ghost" href="[[L:book/]]?service=video">Start a Single Shot</a>
  </article>
  <article class="card price featured">
    <span class="badge">Built for paid social</span>
    <h3>Hook Pack</h3>
    <p class="amt">From $2,500<small>per project · paid social &amp; A/B testing</small></p>
    <p class="time">7–10 business days</p>
    <ul><li>1× 30s hero spot + 2× 15s modular hook / body / CTA cutdowns (or Remotion automated variants)</li><li>AI voiceover (ElevenLabs) + custom sound design</li><li>3 structured rounds: Direction, Refinement, Polish</li><li>Meta, TikTok &amp; Shorts ready</li></ul>
    <a class="btn btn-primary" href="[[L:book/]]?service=video">Start a Hook Pack</a>
  </article>
  <article class="card price">
    <h3>Signature Brand Film</h3>
    <p class="amt">From $5,000<small>per project</small></p>
    <p class="time">14–21 business days</p>
    <ul><li>1× 60–90s hero film + 4× 15–30s short-form derivatives</li><li>Frame-consistent character &amp; product locking</li><li>Original score + full sound design</li><li>3 structured revision rounds · full 4K masters</li></ul>
    <a class="btn btn-ghost" href="[[L:book/]]?service=video">Start a Brand Film</a>
  </article>
  <article class="card price">
    <h3>Cinematic Video Retainer</h3>
    <p class="amt">From $7,500<small>per month · weekly delivery</small></p>
    <p class="time">Ongoing</p>
    <ul><li>Up to 8 assets / month (~4 min total runtime)</li><li>5-day first drafts</li><li>Same-week urgent cuts</li><li>Direct Creative Director access</li></ul>
    <a class="btn btn-ghost" href="[[L:book/]]?service=video">Enquire about retainer</a>
  </article>
</div>'''

STACK_PRICES = '''<div class="price-grid">
  <article class="card price systems">
    <h3>AI Workflow Audit &amp; Blueprint</h3>
    <p class="amt">$750 – $1,500<small>one-time · 100% credited to a build started within 30 days</small></p>
    <p class="time">5 business days</p>
    <ul><li>Deep audit of spreadsheets, email sequences, newsletter cadence, flyer design and social publishing</li><li>ROI time-savings model</li><li>Full architecture roadmap</li></ul>
    <a class="btn btn-ghost" href="[[L:book/]]?service=stack">Audit my workflow</a>
  </article>
  <article class="card price systems featured">
    <span class="badge systems">Best start</span>
    <h3>Starter AI Business Stack</h3>
    <p class="amt">$2,500 – $6,500<small>one-time build</small></p>
    <p class="time">2–3 weeks</p>
    <ul><li>1–2 core custom workflows (e.g. Sheets / CRM → branded flyers + lifecycle email &amp; newsletter drafts + social queue)</li><li>Custom ChatGPT / Gemini skills &amp; prompt library</li><li>Zero-training API setup</li><li>Loom handoff training · 100% client ownership</li></ul>
    <a class="btn btn-systems" href="[[L:book/]]?service=stack">Scope a Starter Stack</a>
  </article>
  <article class="card price systems">
    <h3>Growth AI Operations Stack</h3>
    <p class="amt">$7,500 – $18,000<small>one-time build</small></p>
    <p class="time">3–5 weeks</p>
    <ul><li>End-to-end stack linking Sheets / Airtable / CRM</li><li>Automated email &amp; newsletter engine</li><li>Programmatic flyer &amp; Remotion social video templates</li><li>Webhooks, n8n / Make orchestration, error monitoring, team SOPs</li></ul>
    <a class="btn btn-ghost" href="[[L:book/]]?service=stack">Scope a Growth Stack</a>
  </article>
  <article class="card price systems">
    <h3>Stack Care &amp; Optimization</h3>
    <p class="amt">$500 – $1,500<small>per month · optional · cancel anytime</small></p>
    <p class="time">Month-to-month</p>
    <ul><li>Proactive API &amp; webhook monitoring</li><li>Prompt and model upgrades as models evolve</li><li>Monthly workflow refinements</li></ul>
    <a class="btn btn-ghost" href="[[L:book/]]?service=stack">Ask about care plans</a>
  </article>
</div>'''

HYBRID_PRICE = '''<div class="grid g2">
  <article class="card price featured" style="border-color:var(--text-primary)">
    <h3>Creative + AI Systems Partner</h3>
    <p class="amt">Custom from $4,500 – $9,500<small>per month</small></p>
    <p class="time">Monthly partnership</p>
    <ul><li>Monthly cinematic and performance AI video production</li><li>Continuous custom AI business stack automation</li><li>Every hero campaign becomes automated email sequences, newsletters, flyers and Remotion social cutdowns from one sheet</li><li>One Creative Director across film and systems</li></ul>
    <a class="btn btn-primary" href="[[L:book/]]?service=hybrid">Talk about a Hybrid Retainer</a>
  </article>
  <div class="card elevated">
    <span class="eyebrow">Why hybrid</span>
    <h3>Most studios make the film. Most automation shops wire the tools. Almost nobody does both.</h3>
    <p>A hybrid retainer means the campaign film and the system that distributes it are designed together. The hero cut, the 9:16 hooks, the launch email, the newsletter feature and the flyer all come from the same brief and the same source sheet, so nothing gets lost between the creative team and the ops team.</p>
  </div>
</div>'''


def pricing_section(eyebrow='Investment', h2='How much does Baez Studio cost?', start='video'):
    order = {'video': 0, 'stack': 1, 'hybrid': 2}[start]
    sel = ['false', 'false', 'false']
    sel[order] = 'true'
    lede = {'video': 'Video projects start at $1,500 for a Single Shot and run to $7,500 a month for an always-on retainer; AI business stacks start with a $750 audit.',
            'stack': 'Custom AI business stacks start with a $750–$1,500 audit, and builds run $2,500–$18,000 one-time with optional $500–$1,500 monthly care.',
            }.get(start, '')
    if start == 'video' and h2.startswith('How much does Baez'):
        lede = 'Video projects start at $1,500, and custom AI business stacks start with a $750 audit.'
    return '''<section class="section alt" id="pricing" aria-labelledby="pricing-h">
  <div class="wrap">
    <div class="kicker"><div><span class="eyebrow">%s</span><h2 id="pricing-h">%s</h2></div>%s</div>
    <p class="lede mb3">%s Every figure below is a published starting point or typical range, scoped exactly on a free 15-minute call.</p>
    <div data-tabs>
      <div class="tabs" role="tablist" aria-label="Pricing categories">
        <button class="tab" role="tab" id="t-video" aria-controls="p-video" aria-selected="%s" type="button">AI Video</button>
        <button class="tab systems" role="tab" id="t-stack" aria-controls="p-stack" aria-selected="%s" type="button">AI Business Stacks</button>
        <button class="tab hybrid" role="tab" id="t-hybrid" aria-controls="p-hybrid" aria-selected="%s" type="button">Hybrid Studio Retainer</button>
      </div>
      <section class="panel" id="p-video" role="tabpanel" aria-labelledby="t-video">
        <h3 class="panel-title tabbed mb2">Cinematic AI Video Packages</h3>
        %s
      </section>
      <section class="panel" id="p-stack" role="tabpanel" aria-labelledby="t-stack">
        <h3 class="panel-title tabbed mb2">Custom AI Business Stack Packages</h3>
        %s
      </section>
      <section class="panel" id="p-hybrid" role="tabpanel" aria-labelledby="t-hybrid">
        <h3 class="panel-title tabbed mb2">Hybrid Growth Retainer</h3>
        %s
      </section>
    </div>
    <p class="note mt3"><strong>Founding AI-Stack Partner slots:</strong> a limited number of stack builds are taken each quarter so every system gets senior, hands-on architecture. Backed by Josh Baez's 15+ years of commercial production since 2008.</p>
  </div>
</section>''' % (eyebrow, h2, UPDATED, lede, sel[0], sel[1], sel[2], VIDEO_PRICES, STACK_PRICES, HYBRID_PRICE)


OWNERSHIP = '''<div class="own">
  <span class="eyebrow systems">Ownership &amp; privacy</span>
  <h3>You own everything. Your data trains nothing.</h3>
  <ul class="mt2">
    <li><strong>100% commercial rights</strong> to every finished 4K video deliverable on final payment.</li>
    <li><strong>100% ownership</strong> of custom AI workflows, prompts, scripts and templates. No proprietary platform, no lock-in.</li>
    <li><strong>Your accounts, your keys.</strong> Workflows run on client-owned Google Workspace, API and automation accounts.</li>
    <li><strong>Zero-training APIs.</strong> Business-tier OpenAI, Google and Anthropic APIs and Workspace DPA terms, so your data is not used to train models.</li>
  </ul>
</div>'''

FLOW = '''<div class="flow" role="img" aria-label="Diagram: one source of truth, such as a Google Sheet, Airtable base or CRM, feeds an AI workflow layer that produces lifecycle emails, newsletters, branded flyers, social posts and Remotion video variants.">
  <div class="node source"><span class="mono">Source of truth</span><strong>Google Sheets · Airtable · CRM</strong><small>Products, events, offers, leads, intake forms</small></div>
  <div class="arrow" aria-hidden="true">→</div>
  <div>
    <div class="node mb2"><span class="mono">AI workflow layer</span><strong>Custom GPT / Gemini / Claude + n8n or Make</strong><small>Your brand voice, prompts and templates, with human approval gates</small></div>
    <div class="outputs">
      <div class="node"><span class="mono">Out</span><strong>Lifecycle &amp; outbound email</strong></div>
      <div class="node"><span class="mono">Out</span><strong>Newsletter drafts</strong></div>
      <div class="node"><span class="mono">Out</span><strong>Branded flyers</strong></div>
      <div class="node"><span class="mono">Out</span><strong>Social queue</strong></div>
      <div class="node"><span class="mono">Out</span><strong>Remotion video variants</strong></div>
    </div>
  </div>
</div>'''


def cal_embed(height=700):
    return '''<div class="cal-embed">
  <iframe src="https://cal.com/%s?embed=true&theme=dark&layout=month_view" loading="lazy" title="Book a 15-minute discovery call with Josh Baez" style="height:%dpx"></iframe>
  <noscript><div class="cal-fallback"><p>Open the calendar at <a href="https://cal.com/%s">cal.com/%s</a>.</p></div></noscript>
</div>
<p class="form-note">Calendar not loading? <a href="https://cal.com/%s" target="_blank" rel="noopener">Open it in a new tab</a> or email <a href="mailto:%s">%s</a>.</p>''' % (
        SITE['cal'], height, SITE['cal'], SITE['cal'], SITE['cal'], SITE['email'], SITE['email'])


def brief_form(compact=False):
    return '''<form class="card" action="%s" method="POST" data-brief>
  <input type="hidden" name="_subject" value="New project brief from baez.studio">
  <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
  <div class="field"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
  <div class="field"><label for="f-co">Company or brand</label><input id="f-co" name="company" autocomplete="organization"></div>
  <fieldset>
    <legend>What do you need?</legend>
    <div class="choice">
      <label><input type="radio" name="service" value="video" required> Cinematic AI Video</label>
      <label><input type="radio" name="service" value="stack"> Custom AI Business Stack</label>
      <label><input type="radio" name="service" value="hybrid"> Both / Hybrid Growth Retainer</label>
    </div>
  </fieldset>
  <div class="cond" data-for="video hybrid">
    <p class="mono">Video details</p>
    <div class="field"><label for="f-vtype">Project type</label>
      <select id="f-vtype" name="video_type"><option value="">Choose one</option><option>Single Shot (from $1,500)</option><option>Hook Pack (from $2,500)</option><option>Signature Brand Film (from $5,000)</option><option>Cinematic Video Retainer (from $7,500/mo)</option><option>Not sure yet</option></select></div>
    <div class="field"><label for="f-plat">Where will it run?</label><input id="f-plat" name="platforms" placeholder="Meta, TikTok, YouTube, website, event screen…"></div>
    <div class="field"><label for="f-date">Launch date or deadline</label><input id="f-date" name="deadline" placeholder="e.g. March 14, or flexible"></div>
  </div>
  <div class="cond" data-for="stack hybrid">
    <p class="mono">Workflow details</p>
    <div class="field"><label for="f-team">Team size</label>
      <select id="f-team" name="team_size"><option value="">Choose one</option><option>1–9</option><option>10–49</option><option>50–249</option><option>250+</option></select></div>
    <div class="field"><label for="f-tools">Tools you use today</label><input id="f-tools" name="tools" placeholder="Google Sheets, HubSpot, Mailchimp, Canva, Airtable…"></div>
    <div class="field"><label for="f-hours">Hours per week lost to the task you want automated</label><input id="f-hours" name="hours_per_week" inputmode="numeric" placeholder="e.g. 12"></div>
  </div>
  <div class="field"><label for="f-msg">Tell us about the project</label><textarea id="f-msg" name="message" required placeholder="Goal, audience, references, budget range, anything under NDA."></textarea></div>
  <div class="field"><label for="f-budget">Budget range</label>
    <select id="f-budget" name="budget"><option value="">Prefer to discuss</option><option>Under $2,500</option><option>$2,500 – $5,000</option><option>$5,000 – $10,000</option><option>$10,000 – $20,000</option><option>$20,000+</option></select></div>
  <button class="btn btn-primary" type="submit">Send project brief</button>
  <p class="form-note">A reply within one business day, from Josh directly. Under NDA? Say so and nothing gets shared.</p>
</form>''' % SITE['formspree']


def hero_video(play=True):
    return '''<div class="hero-media">
  <video data-ambient autoplay muted loop playsinline preload="metadata" width="1280" height="720" poster="[[A:assets/media/hero-poster.webp]]" aria-label="Silent ambient loop of the Baez Studio robot mascot in flight">
    <source src="[[A:assets/media/hero-loop.webm]]" type="video/webm">
    <source src="[[A:assets/media/hero-loop.mp4]]" type="video/mp4">
  </video>
  %s
</div>''' % ('<a class="btn btn-ghost btn-sm play" href="https://vimeo.com/%s" data-reel style="background:rgba(10,10,12,.7)">▶ Watch 90s Showreel</a>' % SITE['vimeo'] if play else '')


HERO_PRELOAD = '<link rel="preload" as="image" href="[[A:assets/media/hero-poster.avif]]" type="image/avif" fetchpriority="high">'

CTA = '''<section class="section tight"><div class="wrap"><div class="cta-band">
  <span class="eyebrow">Next step</span>
  <h2>Book a 15-minute <em>discovery call.</em></h2>
  <p class="lede">Bring the launch, the campaign or the spreadsheet that eats your week. You leave with a scope, a price range and a timeline, even if we never work together.</p>
  <div class="btn-row"><a class="btn btn-primary" href="[[L:book/]]">Book a 15-Min Discovery Call →</a><a class="btn btn-ghost" href="mailto:%s">%s</a></div>
</div></div></section>''' % (SITE['email'], SITE['email'])

SHOWREEL_LD = {
    "@context": "https://schema.org", "@type": "VideoObject",
    "name": "Baez Studio Showreel 2026",
    "description": "Showreel of cinematic AI video by Baez Studio: brand films, brand revivals, game and lore cinematics and campaign spots, directed and edited by Josh Baez.",
    "thumbnailUrl": ["https://baez.studio/og-card.png", "https://baez.studio/assets/media/hero-poster.webp"],
    "uploadDate": "2026-05-23T09:00:00-04:00",
    "duration": "PT1M30S",
    "embedUrl": "https://player.vimeo.com/video/1194564875",
    "url": "https://baez.studio/work/showreel-2026/",
    "creator": {"@type": "Person", "name": "Josh Baez", "url": "https://baez.studio/about/"},
    "publisher": {"@id": "https://baez.studio/#studio"},
    "potentialAction": {"@type": "SeekToAction", "target": "https://vimeo.com/1194564875#t={seek_to_second_number}s", "startOffset-input": "required name=seek_to_second_number"},
}

# ---------------------------------------------------------------- FAQs

HOME_FAQS = [
    ("What does Baez Studio do?",
     "Baez Studio makes cinematic AI video for brands and builds custom AI business stacks that automate the spreadsheets, emails, newsletters, flyers and social posts behind growth. Both are directed by Josh Baez, a commercial editor with 15+ years of experience."),
    ("How much does a cinematic AI video cost?",
     "A Single Shot starts at $1,500, a Hook Pack at $2,500, a Signature Brand Film at $5,000 and a Cinematic Video Retainer at $7,500 per month. Each price includes original sound, structured revisions and 4K masters with 9:16, 1:1 and 16:9 exports."),
    ("How much does a custom AI business stack cost?",
     "Most clients start with a $750–$1,500 Workflow Audit, credited in full toward a build started within 30 days. Starter Stacks run $2,500–$6,500, Growth Operations Stacks $7,500–$18,000, and optional care plans $500–$1,500 per month."),
    ("Who owns the videos, prompts and workflows?",
     "You do. Clients receive full commercial rights to finished video and 100% ownership of custom workflows, prompts, scripts and connected accounts on final payment, with no vendor lock-in."),
    ("Is Baez Studio a new studio?",
     "The studio brand is recent; the craft is not. Josh Baez has worked in commercial, social and live-event production since 2008, including Beam Suntory and a confidential consumer brand in California, with campaigns that regularly reach six- and seven-figure view counts."),
    ("Where is Baez Studio based?",
     "The studio works from two Midwest home bases, Ann Arbor, Michigan and Fort Wayne, Indiana, and delivers remotely to B2B, tech, consumer and gaming brands worldwide. In-person shoots and workshops are available in both regions."),
]

VIDEO_FAQS = [
    ("How does AI cinematic video compare to traditional 3D production?",
     "AI cinematic production generates photoreal scenes, characters and environments from references and prompts, then a human editor composites, grades and scores them. It typically reaches finished 4K in days instead of the weeks a 3D pipeline needs, at a fraction of the crew cost, while 3D still wins for engineering-accurate product CAD."),
    ("How long does an AI video project take?",
     "A Single Shot takes 5–7 business days, a Hook Pack 7–10, and a Signature Brand Film 14–21. Retainer clients get first drafts within 5 business days and same-week urgent cuts."),
    ("Which AI and editing tools do you use?",
     "Generative work runs through Runway, Sora, Veo, Higgsfield and ComfyUI, with ElevenLabs for voice. Every project is finished in Premiere Pro, DaVinci Resolve or After Effects, and Remotion handles programmatic variants."),
    ("How do you keep characters and products consistent across shots?",
     "Signature Brand Films use reference locking: approved character sheets, product plates and style frames feed every generation, and anything that drifts is composited or rebuilt by hand in the edit. Inconsistent shots never reach your review link."),
    ("What is a Remotion programmatic video variant?",
     "Remotion renders video from code and data, so one approved template can output dozens of variants with different hooks, prices, cities or product names. It is ideal for A/B testing paid social without re-editing every cut."),
    ("How many revisions are included?",
     "Single Shot includes two rounds. Hook Pack and Signature Brand Film include three structured rounds: Direction, Refinement and Polish. Revisions are built into the timeline, never billed as extras."),
    ("Do you label AI-generated or speculative work?",
     "Yes. Spec pieces made to demonstrate a style are labelled Spec Ad Showcase in the portfolio, and clients choose how to disclose AI use in their own campaigns, in line with platform policies."),
]

STACK_FAQS = [
    ("How much does a custom AI business stack cost?",
     "A Workflow Audit & Blueprint costs $750–$1,500 and is credited toward any build started within 30 days. Starter Stacks are $2,500–$6,500, Growth AI Operations Stacks are $7,500–$18,000, and optional Stack Care runs $500–$1,500 per month."),
    ("What is a custom AI business stack?",
     "It is a set of AI workflows built around your own tools, typically a Google Sheet, Airtable base or CRM, that drafts emails, newsletters, flyers and social posts in your brand voice. Your team reviews and approves; the repetitive formatting, copying and scheduling disappears."),
    ("Is our business data used to train AI models?",
     "No. Stacks use business-tier APIs and Google Workspace under their data processing terms, which exclude customer data from model training, and everything runs on accounts your company owns."),
    ("Which businesses is this a fit for?",
     "Growth-focused small businesses and companies with roughly 10 to 250+ employees that run marketing or operations out of spreadsheets, a CRM and a shared inbox. If someone on your team spends 10+ hours a week copying data into templates, it is a fit."),
    ("What happens if an API or model changes?",
     "Every build ships with error alerts and written SOPs. On a Stack Care plan, Baez Studio monitors webhooks and APIs, upgrades prompts and models as vendors release new versions, and refines workflows monthly."),
    ("Do we need technical staff to run it?",
     "No. Each handoff includes recorded Loom training and plain-language SOPs. Workflows run from familiar tools like Sheets, Gmail and Slack, with approval steps a non-technical marketer can manage."),
]

ABOUT_FAQS = [
    ("Who is Josh Baez?",
     "Josh Baez is the founder and Creative Director of Baez Studio: a creative producer, performance video editor and AI production systems architect with 15+ years of commercial post-production since 2008 and a B.A. in Digital Arts from Point Park University."),
    ("Why does human editorial taste matter in AI video?",
     "Generative tools produce shots; they do not decide which shot earns the cut, where the beat lands or when to hold on a face. That judgment is what separates a film from a pile of renders, and it is what clients hire Josh for."),
]

# ---------------------------------------------------------------- pages

HOME = '''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="pill"><span class="dot" aria-hidden="true"></span>15+ Years Commercial Post · Generative Cinema &amp; Custom AI Business Stacks · Ann Arbor · Fort Wayne · Worldwide</p>
      <h1>Cinematic AI Video &amp; Custom AI Systems — <em>Directed by Craft,</em> Engineered for Speed.</h1>
      <p class="lede">Baez Studio pairs 15+ years of commercial editing with generative AI compositing, Remotion programmatic video, and bespoke AI business workflows, delivering 4K brand campaigns up to 3x faster and automating the spreadsheets, emails, newsletters, flyers, and social pipelines behind your growth.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="[[L:book/]]">Book a 15-Min Discovery Call →</a>
        <a class="btn btn-ghost" href="https://vimeo.com/%(vimeo)s" data-reel>▶ Watch 90s Showreel</a>
      </div>
      <div class="hero-meta"><span>4K masters</span><span>100%% client ownership</span><span>Reply in 1 business day</span></div>
    </div>
    %(hero)s
  </div>
</section>

<section class="section tight" aria-labelledby="pillars-h">
  <div class="wrap">
    <h2 id="pillars-h" class="sr-only">Two services</h2>
    %(pillars)s
  </div>
</section>

<section class="section" aria-labelledby="switch-h">
  <div class="wrap">
    <span class="eyebrow">Choose your path</span>
    <h2 id="switch-h">Which service do you need: <em>video</em> or <em>systems?</em></h2>
    <p class="lede mb3">If the problem is attention, you need the film. If the problem is the hours your team spends producing everything around the film, you need the stack. Many clients need both.</p>
    <div data-tabs>
      <div class="tabs" role="tablist" aria-label="Service switcher">
        <button class="tab" role="tab" id="s-video" aria-controls="sp-video" aria-selected="true" type="button">Cinematic AI Video</button>
        <button class="tab systems" role="tab" id="s-stack" aria-controls="sp-stack" aria-selected="false" type="button">Custom AI Business Stacks</button>
      </div>
      <section class="panel" id="sp-video" role="tabpanel" aria-labelledby="s-video">
        <div class="split">
          <div>
            <h3 class="panel-title">Cinematic AI Video &amp; Programmatic Video</h3>
            <table class="mt2"><caption>What each video format is for</caption>
              <thead><tr><th scope="col">Format</th><th scope="col">Best for</th></tr></thead>
              <tbody>
                <tr><td>Brand Films</td><td>Launches, founder stories, homepage hero films</td></tr>
                <tr><td>Brand Revivals</td><td>Re-introducing an established brand with cinematic weight</td></tr>
                <tr><td>Lore &amp; Worlds</td><td>Game trailers, factions, characters, origin stories</td></tr>
                <tr><td>Hook Packs</td><td>Paid social on Meta, TikTok and YouTube with A/B-ready hooks</td></tr>
                <tr><td>Remotion Variants</td><td>Dozens of data-driven versions from one approved template</td></tr>
              </tbody></table>
            <a class="link-arrow cinema mt2" style="display:inline-block" href="[[L:video-production/]]">See the full video service</a>
          </div>
          <figure class="frame mt0" style="margin:0"><img src="[[A:assets/media/cellar-4.webp]]" width="1100" height="614" loading="lazy" decoding="async" alt="Graded final frame of a wine bottle on a stone plinth under cellar light beams, from a Baez Studio spec ad"><span class="spec">Spec Ad Showcase</span></figure>
        </div>
      </section>
      <section class="panel" id="sp-stack" role="tabpanel" aria-labelledby="s-stack">
        <h3 class="panel-title">Custom AI Business Stacks</h3>
        <p class="secondary measure">One source of truth feeds every channel. Update a row in the sheet and the workflow drafts the email, the newsletter block, the branded flyer and the social post, then waits for your approval.</p>
        <div class="mt2">%(flow)s</div>
        <a class="link-arrow mt2" style="display:inline-block" href="[[L:ai-business-stacks/]]">See how a stack is built</a>
      </section>
    </div>
  </div>
</section>

<section class="section alt" aria-labelledby="proof-h">
  <div class="wrap">
    <div class="kicker"><div><span class="eyebrow">Proof</span><h2 id="proof-h">Recent <em>work.</em></h2></div><a class="btn btn-ghost" href="[[L:work/]]">View all work</a></div>
    <div class="work-grid">
      <a class="work-card" href="[[L:work/showreel-2026/]]"><div class="frame"><img src="[[A:assets/media/hero-poster.webp]]" width="1280" height="720" loading="lazy" decoding="async" alt="Still from the Baez Studio 2026 showreel"></div><div class="meta"><span class="tag cinema">Brand Films</span><span class="tag cinema">Lore &amp; Worlds</span></div><h3>Showreel 2026</h3><p>Ninety seconds of brand films, revivals and game cinematics.</p></a>
      <a class="work-card" href="[[L:work/cellar-reserve-spec/]]"><div class="frame"><img src="[[A:assets/media/cellar-1.webp]]" width="1100" height="614" loading="lazy" decoding="async" alt="Brief board with a wine bottle reference and pinned storyboard"><span class="spec">Spec Ad Showcase</span></div><div class="meta"><span class="tag cinema">Brand Films</span></div><h3>Cellar Reserve: brief to 4K master</h3><p>A premium wine spot, shown stage by stage.</p></a>
      <a class="work-card" href="[[L:work/studio-content-engine/]]"><div class="frame" style="display:grid;place-items:center;background:var(--bg-elevated)"><span class="mono" style="color:var(--accent-systems);font-size:14px">SHEET → EMAIL · FLYER · SOCIAL</span></div><div class="meta"><span class="tag systems">AI Business Stacks</span></div><h3>Studio Content Engine</h3><p>The in-house stack that runs Baez Studio's own publishing.</p></a>
    </div>
  </div>
</section>

<section class="section" id="process" aria-labelledby="process-h">
  <div class="wrap">
    <span class="eyebrow">Process</span>
    <h2 id="process-h">How does a project with Baez Studio work?</h2>
    <p class="lede mb3">Four steps, the same for film and for systems. Scope is locked in writing before any frame is rendered or any workflow is wired.</p>
    <ol class="steps">
      <li><h3>Brief</h3><p>A 15-minute call or a five-minute form. You get a yes, a no, or exactly what it would take, within one business day.</p></li>
      <li><h3>Concept</h3><p>References, storyboard or workflow blueprint, deliverables and price, agreed in writing.</p></li>
      <li><h3>Production</h3><p>Josh directs every generation and every automation, with review links as work lands, not at the end.</p></li>
      <li><h3>Delivery</h3><p>4K masters in every aspect ratio, or a running stack with Loom training and SOPs. All of it yours.</p></li>
    </ol>
  </div>
</section>

%(pricing)s

<section class="section" aria-labelledby="founder-h">
  <div class="wrap">
    <div class="founder">
      <div class="mascot"><video data-lazy data-autoplay muted loop playsinline preload="none" width="720" height="720" aria-label="Baez Studio mascot waving"><source data-src="[[A:contact-mascot.mp4]]" type="video/mp4"></video></div>
      <div>
        <span class="eyebrow cinema">Founder</span>
        <h2 id="founder-h">Directed by Josh Baez, <em>since 2008.</em></h2>
        <p class="lede">Creative producer, performance video editor and AI production systems architect. B.A. in Digital Arts, Point Park University. Past production roles include Beam Suntory and a confidential consumer brand in California.</p>
        <a class="link-arrow cinema" href="[[L:about/]]">Read Josh's story</a>
      </div>
    </div>
    <div class="stats mt3">
      <div class="stat"><b>15+</b><span>years in commercial, social and live-event production</span></div>
      <div class="stat"><b>6–7</b><span>figure organic and paid view counts on multi-platform campaigns</span></div>
      <div class="stat"><b>~60%%</b><span>faster VFX and post turnaround with AI-assisted workflows</span></div>
      <div class="stat"><b>3x</b><span>production speed on campaign deliverables</span></div>
    </div>
  </div>
</section>

<section class="section alt" id="book" aria-labelledby="book-h">
  <div class="wrap">
    <span class="eyebrow">Book</span>
    <h2 id="book-h">Book a call or <em>send a brief.</em></h2>
    <p class="lede mb3">Pick a 15-minute slot on the calendar, or send the brief and Josh will reply within one business day.</p>
    <div class="book-grid">
      %(cal)s
      %(form)s
    </div>
  </div>
</section>

<section class="section" aria-labelledby="faq-h">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2 id="faq-h">Questions, <em>answered.</em></h2>
    [[FAQ]]
  </div>
</section>

%(cta)s''' % {
    'vimeo': SITE['vimeo'], 'hero': hero_video(False), 'pillars': PILLARS, 'flow': FLOW,
    'pricing': pricing_section(), 'cal': '<div>' + cal_embed(640) + '</div>', 'form': brief_form(), 'cta': CTA,
}

VIDEO = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / Video Production</p>
    <span class="eyebrow cinema mt2">Pillar 01</span>
    <h1>Cinematic AI Video <em>&amp; Programmatic Video</em></h1>
    <p class="lede">Baez Studio produces brand films, brand revivals, game and lore cinematics, and paid-social hook packs using generative AI compositing finished by a 15-year commercial editor. Projects start at $1,500 and deliver 4K masters in 5 to 21 business days.</p>
    <div class="btn-row mt2"><a class="btn btn-primary" href="[[L:book/]]?service=video">Book a 15-Min Discovery Call →</a><a class="btn btn-ghost" href="https://vimeo.com/%(vimeo)s" data-reel>▶ Watch 90s Showreel</a></div>
    %(updated)s
  </div>
</section>

<section class="section" aria-labelledby="what-h">
  <div class="wrap">
    <h2 id="what-h">What kinds of AI video does Baez Studio make?</h2>
    <p class="lede mb3">Six formats, each built for a specific job. Every one is directed by a human and finished in a professional NLE, never exported straight from a generator.</p>
    <div class="grid g3">
      <div class="card"><span class="icon-num">01</span><h3>Brand Films</h3><p>Product launches, founder narratives and category campaigns. The film that lives on the homepage, opens the keynote and closes the pitch deck.</p></div>
      <div class="card"><span class="icon-num">02</span><h3>Brand Revivals</h3><p>Re-introduce an established brand with full cinematic weight, so long-time customers feel they are discovering it for the first time.</p></div>
      <div class="card"><span class="icon-num">03</span><h3>Lore &amp; Worlds</h3><p>Game trailers and world-building films: characters, factions, origin stories. The asset that turns an audience into a community.</p></div>
      <div class="card"><span class="icon-num">04</span><h3>Performance Hook Packs</h3><p>Modular hook, body and CTA cuts for Meta, TikTok and YouTube Shorts, built so your media buyer can test openings without a re-edit.</p></div>
      <div class="card"><span class="icon-num">05</span><h3>Generative Compositing</h3><p>Runway, Sora, Veo, Higgsfield and ComfyUI plates composited over live action or product shots in After Effects and Resolve.</p></div>
      <div class="card"><span class="icon-num">06</span><h3>Remotion Programmatic Video</h3><p>Code-driven templates that render dozens of on-brand variants from a spreadsheet: new prices, cities, offers or product names in minutes.</p></div>
    </div>
  </div>
</section>

<section class="section alt" aria-labelledby="flow-h">
  <div class="wrap">
    <h2 id="flow-h">How is an AI video produced, step by step?</h2>
    <p class="lede mb3">Brief, concept, production, delivery. Scope is locked before rendering starts, and revisions are scheduled into the timeline.</p>
    <ol class="steps">
      <li><h3>Brief</h3><p>Goals, audience, platforms, deadline and references. A one-day answer on fit, scope and price.</p></li>
      <li><h3>Concept</h3><p>Script, storyboard, style frames and locked character or product references, approved in writing.</p></li>
      <li><h3>Production</h3><p>Generation, compositing, edit, score and sound design, with review links as each stage lands.</p></li>
      <li><h3>Delivery</h3><p>4K master plus 9:16, 1:1 and 16:9 exports, captioned versions and project files on request.</p></li>
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="ba-h">
  <div class="wrap">
    <h2 id="ba-h">What does "before and after" look like on a real spot?</h2>
    <p class="lede mb3">From the <a href="[[L:work/cellar-reserve-spec/]]">Cellar Reserve spec ad</a>: four frames from the brief board to the graded 4K master.</p>
    <div class="ba">
      <figure><div class="frame"><img src="[[A:assets/media/cellar-1.webp]]" width="1100" height="614" loading="lazy" decoding="async" alt="Brief board with bottle reference and storyboard"></div><figcaption><strong>01 · Brief</strong>Bottle reference, mood and shot list pinned on day one.</figcaption></figure>
      <figure><div class="frame"><img src="[[A:assets/media/cellar-2.webp]]" width="1100" height="614" loading="lazy" decoding="async" alt="Hand-drawn storyboard with shot labels and colour palette"></div><figcaption><strong>02 · Storyboard</strong>Shot labels, palette and pacing approved before rendering.</figcaption></figure>
      <figure><div class="frame"><img src="[[A:assets/media/cellar-3.webp]]" width="1100" height="614" loading="lazy" decoding="async" alt="Artist building the bottle silhouette and palette on screen"></div><figcaption><strong>03 · Generative compositing</strong>Bottle locked as a reference plate; cellar generated around it.</figcaption></figure>
      <figure><div class="frame"><img src="[[A:assets/media/cellar-4.webp]]" width="1100" height="614" loading="lazy" decoding="async" alt="Final graded frame of the bottle on a stone plinth with light beams"></div><figcaption><strong>04 · Graded 4K master</strong>Light beams, dust and grade finished in Resolve.</figcaption></figure>
    </div>
  </div>
</section>

<section class="section alt" aria-labelledby="hook-h">
  <div class="wrap split">
    <div>
      <h2 id="hook-h">How is a paid-social Hook Pack structured?</h2>
      <p class="lede">A Hook Pack splits every spot into swappable hook, body and CTA segments, so one shoot becomes a test matrix. Three hooks against one body give your media buyer three clean A/B tests from day one.</p>
      <table class="mt2"><caption>Anatomy of a 15-second cutdown</caption>
        <thead><tr><th scope="col">Segment</th><th scope="col">Length</th><th scope="col">Job</th></tr></thead>
        <tbody><tr><td>Hook</td><td>0–3s</td><td>Stop the thumb: motion, contrast, a question</td></tr>
        <tr><td>Body</td><td>3–12s</td><td>Show the product doing the thing</td></tr>
        <tr><td>CTA</td><td>12–15s</td><td>One action, on-screen and in VO</td></tr></tbody></table>
    </div>
    <div>
      <p class="mono mb2">Every package ships in</p>
      <div class="formats"><div class="f916">9:16</div><div class="f11">1:1</div><div class="f169">16:9</div></div>
      <p class="secondary mt2">Meta Reels and Stories, TikTok, YouTube Shorts, YouTube in-stream, LinkedIn and X, plus a 4K master for web and events.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="cmp-h">
  <div class="wrap">
    <h2 id="cmp-h">How does AI cinematic video compare to traditional production?</h2>
    <p class="lede mb3">AI production reaches finished 4K in days at a fraction of the crew cost. Traditional shoots and 3D still win for some jobs, and Josh will tell you which one yours is.</p>
    <div class="table-wrap"><table>
      <thead><tr><th scope="col">Factor</th><th scope="col">Baez Studio AI production</th><th scope="col">Traditional live-action or 3D</th></tr></thead>
      <tbody>
        <tr><td>Typical timeline</td><td>5–21 business days</td><td>4–12 weeks</td></tr>
        <tr><td>Crew &amp; locations</td><td>Director-editor plus generative tools</td><td>Crew, talent, locations, render farm</td></tr>
        <tr><td>Starting budget</td><td>From $1,500</td><td>Often $15,000+</td></tr>
        <tr><td>Variants for testing</td><td>Remotion templates, dozens per day</td><td>Manual re-edits</td></tr>
        <tr><td>Best when</td><td>Worlds, moods, products in impossible places, fast campaigns</td><td>Real people on camera, CAD-accurate engineering visuals</td></tr>
      </tbody></table></div>
  </div>
</section>

%(pricing)s

<section class="section" aria-labelledby="own-h"><div class="wrap"><h2 id="own-h" class="sr-only">Ownership</h2>%(own)s</div></section>

<section class="section" aria-labelledby="faq-h">
  <div class="wrap">
    <span class="eyebrow cinema">Video FAQ</span>
    <h2 id="faq-h">AI video <em>questions.</em></h2>
    [[FAQ]]
  </div>
</section>
%(cta)s''' % {'vimeo': SITE['vimeo'], 'updated': UPDATED, 'pricing': pricing_section('Video investment', 'How much does a cinematic AI video cost?', 'video'), 'own': OWNERSHIP, 'cta': CTA}

STACKS = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / AI Business Stacks</p>
    <span class="eyebrow systems mt2">Pillar 02</span>
    <h1>Custom AI Business Stacks <em>that your team owns.</em></h1>
    <p class="lede">Baez Studio builds bespoke AI workflows that turn one spreadsheet or CRM into automated lifecycle emails, newsletters, branded flyers and social posts. Builds start at $2,500 after a $750 audit, typically reclaim 10–15 hours a week, and run on accounts you own.</p>
    <div class="btn-row mt2"><a class="btn btn-systems" href="[[L:book/]]?service=stack">Audit Your Workflow →</a><a class="btn btn-ghost" href="#roi">See the ROI math</a></div>
    %(updated)s
  </div>
</section>

<section class="section" aria-labelledby="prob-h">
  <div class="wrap split">
    <div>
      <h2 id="prob-h">What problem does a custom AI business stack solve?</h2>
      <p class="lede">It removes the copy-paste layer between your data and your marketing. If someone exports a sheet, reformats it into a flyer, rewrites it as an email, then reposts it to three social accounts, that whole chain can run itself with a human approval step.</p>
    </div>
    <div class="card">
      <h3>Built for</h3>
      <ul class="secondary">
        <li>Growth-focused SMBs and teams of 10 to 250+ employees</li>
        <li>Marketing and ops teams living in Google Workspace, Airtable or a CRM</li>
        <li>Event, retail, hospitality, healthcare and B2B teams with weekly content cadences</li>
        <li>Agencies that need a white-label automation partner</li>
      </ul>
      <p class="mb0"><strong>Not built for:</strong> a generic chatbot on your homepage. This is operations, not novelty.</p>
    </div>
  </div>
</section>

<section class="section alt" aria-labelledby="how-h">
  <div class="wrap">
    <h2 id="how-h">How does one source of truth power every channel?</h2>
    <p class="lede mb3">Every stack starts from the place your data already lives. A new row, status change or form submission triggers the AI workflow layer, which drafts each output in your brand voice and queues it for approval.</p>
    %(flow)s
    <ol class="steps systems mt3">
      <li><h3>Audit</h3><p>Map every manual step, tool and hand-off. Measure hours per week per task.</p></li>
      <li><h3>Blueprint</h3><p>Architecture diagram, prompt library plan, approval gates and an ROI model.</p></li>
      <li><h3>Build</h3><p>Custom GPT / Gemini / Claude skills, n8n or Make orchestration, templates and error alerts.</p></li>
      <li><h3>Handoff</h3><p>Loom training, written SOPs and admin access transferred to your accounts.</p></li>
    </ol>
  </div>
</section>

<section class="section" id="roi" aria-labelledby="roi-h">
  <div class="wrap split">
    <div>
      <h2 id="roi-h">How much time does an AI business stack actually save?</h2>
      <p class="lede">For a typical weekly content cadence, a Starter Stack replaces 10–15 hours of manual work per week. At a fully loaded $45 per hour, that is roughly $23,000–$35,000 a year in reclaimed time, against a one-time build of $2,500–$6,500.</p>
      <p class="secondary">Worked example: a 25-person regional events company running promotions from a shared Google Sheet. Figures are a planning model; your audit produces your own numbers.</p>
    </div>
    <div>
      <div class="table-wrap"><table>
        <caption>Weekly hours, before and after</caption>
        <thead><tr><th scope="col">Task</th><th scope="col">Manual</th><th scope="col">With stack</th></tr></thead>
        <tbody>
          <tr><td>Spreadsheet syncing &amp; cleanup</td><td>3.5 h</td><td>0.5 h</td></tr>
          <tr><td>Flyer formatting (4/week)</td><td>4 h</td><td>0.5 h</td></tr>
          <tr><td>Newsletter drafting</td><td>3 h</td><td>0.75 h</td></tr>
          <tr><td>Social scheduling (3 channels)</td><td>3 h</td><td>0.5 h</td></tr>
          <tr><td>Lifecycle email updates</td><td>1.5 h</td><td>0.25 h</td></tr>
          <tr><td><strong>Total</strong></td><td><strong>15 h</strong></td><td><strong>2.5 h</strong></td></tr>
        </tbody></table></div>
      <div class="math mt2">12.5 h saved / week × 48 weeks = <b>600 h / year</b><br>600 h × $45 loaded rate = <b>$27,000 / year</b><br>Starter build $4,500 → payback in <b>~8 weeks</b></div>
    </div>
  </div>
</section>

<section class="section alt" aria-labelledby="sec-h">
  <div class="wrap">
    <h2 id="sec-h">How is client data kept secure?</h2>
    <p class="lede mb3">Your data stays in accounts you own, flows only through business-tier APIs that exclude it from model training, and every credential is handed back at the end of the build.</p>
    %(own)s
    <div class="table-wrap mt3"><table>
      <thead><tr><th scope="col">Standard</th><th scope="col">How it is applied</th></tr></thead>
      <tbody>
        <tr><td>Zero-training APIs</td><td>OpenAI, Google and Anthropic business APIs under terms that exclude customer data from training</td></tr>
        <tr><td>Workspace DPA</td><td>Google Workspace automations operate under your organisation's Data Processing Amendment</td></tr>
        <tr><td>Least privilege</td><td>Service accounts scoped to the sheets, folders and inboxes each workflow needs</td></tr>
        <tr><td>Human approval</td><td>Nothing customer-facing sends without an approval step unless you choose otherwise</td></tr>
        <tr><td>Clean exit</td><td>All keys, prompts, templates and docs transferred; studio access removed at handoff</td></tr>
      </tbody></table></div>
  </div>
</section>

%(pricing)s

<section class="section" aria-labelledby="faq-h">
  <div class="wrap">
    <span class="eyebrow systems">AI Stack FAQ</span>
    <h2 id="faq-h">AI business stack <em>questions.</em></h2>
    [[FAQ]]
  </div>
</section>

<section class="section tight"><div class="wrap"><div class="cta-band">
  <span class="eyebrow systems">Audit Your Workflow</span>
  <h2>Where is your team losing <em>10 hours a week?</em></h2>
  <p class="lede">Book a 15-minute call and walk through one recurring task. You will leave with an estimate of hours saved and what a stack would cost to build.</p>
  <div class="btn-row"><a class="btn btn-systems" href="[[L:book/]]?service=stack">Audit Your Workflow →</a><a class="btn btn-ghost" href="mailto:%(email)s">%(email)s</a></div>
</div></div></section>''' % {'updated': UPDATED, 'flow': FLOW, 'own': OWNERSHIP, 'email': SITE['email'],
                             'pricing': pricing_section('Stack investment', 'How much does a custom AI business stack cost?', 'stack')}

WORK_ITEMS = [
    # slug, title, cats, filter-cats, blurb, thumb, spec
    ('showreel-2026', 'Showreel 2026', ['Brand Films', 'Lore & Worlds', 'Paid Social Hooks'], 'brand-films lore paid-social',
     'Ninety seconds of brand films, revivals, game cinematics and campaign spots.', 'assets/media/hero-poster.webp', False),
    ('cellar-reserve-spec', 'Cellar Reserve: brief to 4K master', ['Brand Films'], 'brand-films',
     'A premium wine spot shown stage by stage, from brief board to graded master.', 'assets/media/cellar-1.webp', True),
    ('fly-mascot', 'Fly: a studio mascot in motion', ['Lore & Worlds'], 'lore',
     'Character design and animation loops for the Baez Studio mascot, built for web, social and stickers.', 'fly-poster.jpg', False),
    ('studio-content-engine', 'Studio Content Engine', ['AI Business Stacks'], 'stacks',
     'The in-house stack that turns one content sheet into posts, emails and flyers.', None, False),
]


def work_card(slug, title, cats, fcats, blurb, thumb, spec):
    tagcls = lambda c: 'systems' if 'Stack' in c else 'cinema'
    tags = ''.join('<span class="tag %s">%s</span>' % (tagcls(c), c.replace('&', '&amp;')) for c in cats)
    if thumb:
        w, h = (1280, 720) if 'poster' in thumb else (1100, 614)
        media = '<div class="frame"><img src="[[A:%s]]" width="%d" height="%d" loading="lazy" decoding="async" alt="%s">%s</div>' % (
            thumb, w, h, 'Still from ' + title, '<span class="spec">Spec Ad Showcase</span>' if spec else '')
    else:
        media = '<div class="frame" style="display:grid;place-items:center;background:var(--bg-elevated)"><span class="mono" style="color:var(--accent-systems);font-size:14px">SHEET → EMAIL · FLYER · SOCIAL</span></div>'
    return '<a class="work-card" data-cat="%s" href="[[L:work/%s/]]">%s<div class="meta">%s</div><h3>%s</h3><p>%s</p></a>' % (
        fcats, slug, media, tags, title.replace('&', '&amp;'), blurb)


WORK = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / Work</p>
    <h1>Curated proof &amp; <em>case studies.</em></h1>
    <p class="lede">Selected films, spec pieces and AI systems by Baez Studio. Each case study names Josh's exact role, the formats delivered and a full scene breakdown. Speculative commercial pieces are labelled Spec Ad Showcase.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="filters" data-filters hidden role="group" aria-label="Filter work">
      <button class="filter" type="button" data-f="all" aria-pressed="true">All</button>
      <button class="filter" type="button" data-f="brand-films" aria-pressed="false">Brand Films</button>
      <button class="filter" type="button" data-f="paid-social" aria-pressed="false">Paid Social Hooks</button>
      <button class="filter" type="button" data-f="lore" aria-pressed="false">Lore &amp; Worlds</button>
      <button class="filter" type="button" data-f="stacks" aria-pressed="false">AI Business Stacks</button>
    </div>
    <div class="work-grid">
      %s
      <div class="card" data-cat="paid-social brand-films"><span class="eyebrow cinema">Under NDA</span><h3>Client campaigns</h3><p>Much of Josh's paid-social and brand work, including six- and seven-figure-view campaigns, sits under NDA. Ask on a discovery call for a private walkthrough of relevant examples.</p><a class="link-arrow cinema" href="[[L:book/]]">Request a private reel</a></div>
    </div>
  </div>
</section>
%s''' % ('\n      '.join(work_card(*w) for w in WORK_ITEMS), CTA)


def case_page(slug, title, eyebrow, lede, role, formats, brief, breakdown, media, extra='', cat_link=('Video Production', 'video-production/')):
    return '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / <a href="[[L:work/]]">Work</a> / %s</p>
    <span class="eyebrow mt2">%s</span>
    <h1>%s</h1>
    <p class="lede">%s</p>
  </div>
</section>
<section class="section tight">
  <div class="wrap">
    %s
    <div class="grid g3 mt3">
      <div class="card"><span class="eyebrow">Brief</span><p>%s</p></div>
      <div class="card"><span class="eyebrow">Josh's role</span><p>%s</p></div>
      <div class="card"><span class="eyebrow">Formats</span><p>%s</p></div>
    </div>
    %s
    <details class="transcript" open><summary>Scene breakdown &amp; summary</summary><ol>%s</ol></details>
    <p class="mt3"><a class="link-arrow cinema" href="[[L:%s]]">Explore %s</a></p>
  </div>
</section>
%s''' % (title, eyebrow, title, lede, media, brief, role, formats, extra, breakdown, cat_link[1], cat_link[0], CTA)


CASE_SHOWREEL = case_page(
    'showreel-2026', 'Showreel 2026', 'Brand Films · Lore &amp; Worlds · Paid Social',
    'A 90-second cut of Baez Studio\'s cinematic AI work: brand films, brand revivals, game cinematics and campaign spots, directed, composited and edited by Josh Baez.',
    'Director, editor, generative compositor, colourist and sound designer.',
    '4K 16:9 master, 9:16 and 1:1 social cutdowns.',
    'Show the full range of the studio in under two minutes: tone, worlds, products and pacing that a brand can picture its own story inside.',
    '<li>Cold open on a single held frame to set the cinematic tone before any cut.</li><li>Brand film section: product hero shots composited into generated environments.</li><li>Lore &amp; Worlds section: characters, factions and environments built for game and world-building clients.</li><li>Campaign section: fast-cut hooks built in the Hook Pack structure.</li><li>Close on the BAEZ.AI.STUDIO mark and call to action.</li>',
    '<div class="frame"><img src="[[A:assets/media/hero-poster.webp]]" width="1280" height="720" alt="Showreel poster frame" decoding="async"><a class="btn btn-primary play" style="position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%)" href="https://vimeo.com/%s" data-reel>▶ Play showreel</a></div>' % SITE['vimeo'])

CASE_CELLAR = case_page(
    'cellar-reserve-spec', 'Cellar Reserve: brief to 4K master', 'Spec Ad Showcase · Brand Films',
    'A self-initiated spec ad for a premium wine label, made to show every stage of a Baez Studio production. It is not a paid client commission.',
    'Concept, storyboard, generative compositing, grade and finishing.',
    '4K 16:9 hero frame set; 9:16 and 1:1 crops planned in the storyboard.',
    'Present a single bottle with the weight of a heritage brand: cellar light, dust, stone and time, without a location shoot.',
    '<li>Brief: bottle reference and mood pinned with shot list.</li><li>Storyboard: hand-drawn frames with shot labels and a warm amber palette.</li><li>Production: bottle silhouette locked as a reference plate so the label shape never drifts between generations.</li><li>Compositing: cellar arches, barrels and volumetric light generated around the locked bottle.</li><li>Finish: grade, dust particles and light beams balanced in Resolve for the 4K master.</li>',
    '<div class="frame"><img src="[[A:assets/media/cellar-4.webp]]" width="1100" height="614" alt="Final frame: wine bottle on a stone plinth in a cellar with light beams" decoding="async"><span class="spec">Spec Ad Showcase</span></div>',
    extra='''<h2 class="mt3">Before and after</h2><div class="ba mt2">
      <figure><div class="frame"><img src="[[A:assets/media/cellar-1.webp]]" width="1100" height="614" loading="lazy" alt="Brief board"></div><figcaption><strong>01 · Brief</strong>Reference and shot list.</figcaption></figure>
      <figure><div class="frame"><img src="[[A:assets/media/cellar-2.webp]]" width="1100" height="614" loading="lazy" alt="Storyboard"></div><figcaption><strong>02 · Storyboard</strong>Frames, labels, palette.</figcaption></figure>
      <figure><div class="frame"><img src="[[A:assets/media/cellar-3.webp]]" width="1100" height="614" loading="lazy" alt="Compositing in progress"></div><figcaption><strong>03 · Compositing</strong>Locked bottle plate.</figcaption></figure>
      <figure><div class="frame"><img src="[[A:assets/media/cellar-4.webp]]" width="1100" height="614" loading="lazy" alt="Graded master"></div><figcaption><strong>04 · 4K master</strong>Final grade.</figcaption></figure></div>''')

CASE_FLY = case_page(
    'fly-mascot', 'Fly: a studio mascot in motion', 'Lore &amp; Worlds · Character',
    'Fly is the Baez Studio mascot, a small robot cat designed as a consistent character across web loops, social posts and stickers, showing frame-consistent character locking in practice.',
    'Character design direction, generation, animation clean-up and loop editing.',
    '1080p 16:9 hero loop, 1:1 loop, poster stills.',
    'Create a friendly, ownable character that reads at thumbnail size and stays on-model across every pose and loop.',
    '<li>Character sheet: white and blue shell, cat ears and tail, large blue eyes, locked as the reference for every generation.</li><li>Flight loop: superhero pose, used as this site\'s ambient hero video.</li><li>Wave loop: square format for contact and social use.</li><li>Loops edited forward and back so motion repeats without a visible seam.</li>',
    '''<div class="grid g2"><div class="frame"><video data-lazy data-autoplay muted loop playsinline preload="none" width="1280" height="720" poster="[[A:fly-poster.jpg]]" aria-label="Fly the mascot flying"><source data-src="[[A:assets/media/hero-loop.webm]]" type="video/webm"><source data-src="[[A:assets/media/hero-loop.mp4]]" type="video/mp4"></video></div><div class="frame square" style="aspect-ratio:16/9"><video data-lazy data-autoplay muted loop playsinline preload="none" width="720" height="720" aria-label="Fly the mascot waving" style="object-fit:contain"><source data-src="[[A:contact-mascot.mp4]]" type="video/mp4"></video></div></div>''',
    cat_link=('Video Production', 'video-production/'))

CASE_STACK = case_page(
    'studio-content-engine', 'Studio Content Engine', 'AI Business Stacks · Internal Studio Build',
    'The workflow Baez Studio uses on its own marketing: one Google Sheet of content ideas becomes draft social posts, newsletter blocks and branded flyers, each waiting for approval. It is an internal build, shown as a blueprint.',
    'Architecture, prompt library, automation build and SOPs.',
    'Google Sheet source, n8n workflow, Docs templates, social queue.',
    'Publish consistently across Instagram, X, LinkedIn and email without a full-time social manager.',
    '<li>Source: a Google Sheet with one row per idea (topic, pillar, asset link, target date, status).</li><li>Trigger: status changes to "Ready" and the workflow starts.</li><li>Drafting: a custom GPT with the studio voice guide writes platform-specific captions and a newsletter block.</li><li>Design: a branded flyer template fills headline, date and image automatically.</li><li>Approval: drafts land in a review tab; nothing posts until it is approved.</li><li>Publish &amp; log: approved items are queued and the sheet records links and dates.</li>',
    '<div class="card">' + FLOW + '</div>',
    cat_link=('AI Business Stacks', 'ai-business-stacks/'))

FLY_LD = {
    "@context": "https://schema.org", "@type": "VideoObject", "name": "Fly: Baez Studio mascot flight loop",
    "description": "Ambient loop of Fly, the Baez Studio robot cat mascot, in a superhero flight pose. Character-consistent AI animation.",
    "thumbnailUrl": "https://baez.studio/fly-poster.jpg", "uploadDate": "2026-05-23T09:00:00-04:00", "duration": "PT7S",
    "contentUrl": "https://baez.studio/assets/media/hero-loop.mp4", "url": "https://baez.studio/work/fly-mascot/",
    "creator": {"@type": "Person", "name": "Josh Baez", "url": "https://baez.studio/about/"},
}

LOC_HUB = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / Service Areas</p>
    <h1>Two Midwest bases. <em>Clients worldwide.</em></h1>
    <p class="lede">Baez Studio works from Ann Arbor, Michigan and Fort Wayne, Indiana, with in-person shoots, workshops and planning sessions in both regions, and fully remote delivery everywhere else.</p>
  </div>
</section>
<section class="section">
  <div class="wrap grid g3">
    <a class="card pillar" href="[[L:locations/ann-arbor/]]"><span class="eyebrow cinema">Michigan</span><h3>Ann Arbor, MI</h3><p>Pitch films, technical explainers, Remotion product demos and sales-ops AI stacks for startups, U-M spinouts and B2B SaaS.</p><span class="link-arrow">Ann Arbor services</span></a>
    <a class="card pillar systems" href="[[L:locations/fort-wayne/]]"><span class="eyebrow systems">Indiana</span><h3>Fort Wayne, IN</h3><p>Recruiting films, product storytelling and operations automation for Northeast Indiana makers, healthcare and agencies.</p><span class="link-arrow">Fort Wayne services</span></a>
    <div class="card pillar" style="border-top-color:var(--text-primary)"><span class="eyebrow">Everywhere else</span><h3>Global remote delivery</h3><p>Briefs by call, reviews by frame-accurate links, delivery to your drive. Brands in the US, Europe and beyond work with the studio fully remotely.</p><a class="link-arrow" style="color:var(--text-primary)" href="[[L:book/]]">Book a remote call</a></div>
  </div>
</section>
%s''' % CTA


def svc_ld(name, area, url, desc):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "url": url, "description": desc,
            "provider": {"@id": "https://baez.studio/#studio"}, "areaServed": area,
            "serviceType": ["AI video production", "AI workflow automation"]}


ANN = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / <a href="[[L:locations/]]">Service Areas</a> / Ann Arbor, MI</p>
    <span class="eyebrow cinema mt2">Ann Arbor, Michigan</span>
    <h1>AI video &amp; AI systems for <em>Ann Arbor's builders.</em></h1>
    <p class="lede">Baez Studio helps Ann Arbor startups, University of Michigan research spinouts and B2B SaaS teams explain hard technology fast: investor pitch films, technical explainers, Remotion product demos and AI sales-ops stacks, with in-person sessions in Washtenaw County.</p>
    <div class="btn-row mt2"><a class="btn btn-primary" href="[[L:book/]]">Book an Ann Arbor discovery call →</a></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>What do Ann Arbor startups hire Baez Studio for?</h2>
    <p class="lede mb3">Mostly the moments where a technical team has to make non-technical people believe: a raise, a launch or a first enterprise deal.</p>
    <div class="grid g2">
      <div class="card"><span class="icon-num">Raise</span><h3>Investor pitch films</h3><p>A 60–90 second film for the top of the deck and the demo-day screen. Founders preparing for accelerator demo days, including companies coming through Ann Arbor SPARK and SPARK East programs, use it to make the problem visceral before the first slide.</p></div>
      <div class="card"><span class="icon-num">Explain</span><h3>Technical explainers for spinouts</h3><p>University of Michigan research spinouts often have a breakthrough that takes ten minutes to explain. Generative visuals show the molecule, the sensor or the battery at work in 45 seconds, with copy your scientists sign off on.</p></div>
      <div class="card"><span class="icon-num">Ship</span><h3>Remotion product demos for SaaS</h3><p>B2B SaaS teams ship features weekly. Remotion templates turn each release note into a branded demo clip, so marketing keeps pace with engineering without booking an editor every sprint.</p></div>
      <div class="card"><span class="icon-num systems">Sell</span><h3>Sales &amp; ops AI stacks</h3><p>Lean teams wire their CRM to AI-drafted follow-ups, investor update emails and event flyers for local meetups and conferences, reclaiming founder hours for building.</p></div>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap split">
    <div>
      <h2>How does working together in Ann Arbor look?</h2>
      <p class="lede">Kickoffs can happen in person anywhere around Ann Arbor and the wider Washtenaw County area; production and reviews run remotely so your team never blocks on a meeting.</p>
    </div>
    <div class="table-wrap"><table><thead><tr><th scope="col">Ann Arbor need</th><th scope="col">Starting package</th></tr></thead><tbody>
      <tr><td>Demo-day pitch film</td><td>Signature Brand Film · from $5,000</td></tr>
      <tr><td>Launch teaser + social hooks</td><td>Hook Pack · from $2,500</td></tr>
      <tr><td>Release-note demo engine</td><td>Starter AI Business Stack · $2,500–$6,500</td></tr>
      <tr><td>Investor update + CRM follow-up automation</td><td>Workflow Audit · $750–$1,500</td></tr>
    </tbody></table></div>
  </div>
</section>
<section class="section"><div class="wrap"><h2>Ann Arbor <em>FAQ</em></h2>[[FAQ]]</div></section>
%s''' % CTA

ANN_FAQS = [
    ("Does Baez Studio meet clients in person in Ann Arbor?",
     "Yes. Kickoffs, workshops and planning sessions can happen in person around Ann Arbor and Washtenaw County, while production and reviews run remotely."),
    ("Can you make a pitch film before our demo day?",
     "Yes. A Signature Brand Film takes 14–21 business days and a Hook Pack-style teaser 7–10, so start about four weeks before the date and the schedule is built backwards from it."),
    ("Can you explain deep technical research visually?",
     "Yes. Explainers for research-driven companies are scripted with your technical team, and every claim and visual is approved by them before it is rendered in 4K."),
]

FW = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / <a href="[[L:locations/]]">Service Areas</a> / Fort Wayne, IN</p>
    <span class="eyebrow systems mt2">Fort Wayne, Indiana</span>
    <h1>Cinematic video &amp; automation for <em>Northeast Indiana makers.</em></h1>
    <p class="lede">Baez Studio works with Fort Wayne and Northeast Indiana manufacturers, healthcare organisations, consumer brands and creative agencies: recruiting and product films, AI-assisted post-production overflow, and workflow automation that frees up lean marketing teams.</p>
    <div class="btn-row mt2"><a class="btn btn-systems" href="[[L:book/]]">Book a Fort Wayne discovery call →</a></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>What do Fort Wayne businesses hire Baez Studio for?</h2>
    <p class="lede mb3">Regional makers and mid-size companies need big-brand storytelling and big-company efficiency without big-company headcount.</p>
    <div class="grid g2">
      <div class="card"><span class="icon-num">Make</span><h3>Manufacturer product &amp; recruiting films</h3><p>Show precision parts, plant floors and the people behind them. Generative compositing fills in what a shoot cannot reach, from inside a machine to a product in its end-use environment, and recruiting cuts help fill skilled roles.</p></div>
      <div class="card"><span class="icon-num">Care</span><h3>Healthcare &amp; regional services</h3><p>Patient education, service-line launches and community campaigns with careful, approved messaging, plus automated newsletters and event flyers driven from a single schedule sheet.</p></div>
      <div class="card"><span class="icon-num">Sell</span><h3>Consumer &amp; retail brands</h3><p>Hook Packs and seasonal promotions for local and regional retail, with Remotion variants that swap offers, locations and dates without a re-edit.</p></div>
      <div class="card"><span class="icon-num systems">Partner</span><h3>Overflow for Fort Wayne agencies</h3><p>White-label AI post-production and automation for local creative and marketing agencies: generative compositing, cutdowns and client reporting workflows delivered under your brand, on your timeline.</p></div>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap split">
    <div>
      <h2>Why use an AI-first studio for a manufacturing brand?</h2>
      <p class="lede">Because the best shot is often impossible to film: inside a running press, a part at microscopic scale or a product in a market you have not entered yet. AI compositing delivers those shots in days, finished by an editor who knows when real footage is better.</p>
    </div>
    <div class="table-wrap"><table><thead><tr><th scope="col">Fort Wayne need</th><th scope="col">Starting package</th></tr></thead><tbody>
      <tr><td>Recruiting film + social cuts</td><td>Signature Brand Film · from $5,000</td></tr>
      <tr><td>Trade-show loop + product hooks</td><td>Hook Pack · from $2,500</td></tr>
      <tr><td>Newsletter + flyer automation</td><td>Starter AI Business Stack · $2,500–$6,500</td></tr>
      <tr><td>Agency overflow partnership</td><td>Hybrid Growth Retainer · from $4,500/mo</td></tr>
    </tbody></table></div>
  </div>
</section>
<section class="section"><div class="wrap"><h2>Fort Wayne <em>FAQ</em></h2>[[FAQ]]</div></section>
%s''' % CTA

FW_FAQS = [
    ("Does Baez Studio work on-site in Fort Wayne?",
     "Yes. Planning sessions, plant walk-throughs and workshops can happen in person in Fort Wayne and across Northeast Indiana; production and reviews run remotely."),
    ("Do you partner with Fort Wayne marketing agencies?",
     "Yes. Agencies use Baez Studio as a white-label overflow partner for AI post-production, cutdowns and workflow automation, under the agency's brand and client relationship."),
    ("Can AI video show our product accurately?",
     "Your real product photos and CAD renders are locked as reference plates, so the product stays accurate while environments and motion are generated around it. Anything engineering-critical is checked with your team before delivery."),
]

ABOUT = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / About</p>
    <span class="eyebrow cinema mt2">Founder &amp; Studio Philosophy</span>
    <h1>Josh Baez: <em>15 years of cuts</em> before the first prompt.</h1>
    <p class="lede">Josh Baez is the founder and Creative Director of Baez Studio: a creative producer, performance video editor and AI production systems architect with commercial, social and live-event post-production experience since 2008.</p>
  </div>
</section>
<section class="section">
  <div class="wrap split" style="align-items:start">
    <div>
      <h2>How did Baez Studio start?</h2>
      <ol class="timeline mt2">
        <li><span class="mono">Point Park University</span><strong>B.A. in Digital Arts</strong><p>Pittsburgh. Editing, motion and storytelling fundamentals.</p></li>
        <li><span class="mono">2008 onward</span><strong>Commercial, social &amp; live-event production</strong><p>Fifteen-plus years cutting campaigns, events and branded content.</p></li>
        <li><span class="mono">Pittsburgh, PA</span><strong>Beam Suntory</strong><p>Production work for one of the world's leading spirits companies.</p></li>
        <li><span class="mono">California</span><strong>Confidential consumer brand (NDA)</strong><p>Multi-platform social campaigns regularly reaching six- and seven-figure view counts.</p></li>
        <li><span class="mono">Today</span><strong>Founder, BAEZ.AI.STUDIO</strong><p>Generative cinema and custom AI business stacks, from Ann Arbor, MI and Fort Wayne, IN, for clients worldwide.</p></li>
      </ol>
    </div>
    <div class="stack">
      <div class="mascot" style="width:200px"><video data-lazy data-autoplay muted loop playsinline preload="none" width="720" height="720" aria-label="Baez Studio mascot waving"><source data-src="[[A:contact-mascot.mp4]]" type="video/mp4"></video></div>
      <h2>Why does human editorial taste matter in AI video?</h2>
      <p class="lede">Generators make shots. Editors make films. The difference is judgment: which take earns the cut, where the beat lands, when to hold on a face and when to get out.</p>
      <p class="secondary">Josh uses AI the way a cinematographer uses a lens: to reach shots that used to need a six-figure budget. Every frame is still chosen, timed, graded and scored by a person who has spent fifteen years learning what makes an audience feel something. The same discipline goes into AI business stacks: the tools are new, but the process mapping, quality control and client ownership come from years of shipping real work to real deadlines.</p>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <h2>What is the Baez Studio method?</h2>
    <div class="grid g3 mt2">
      <div class="card"><span class="icon-num">01</span><h3>Story before tools</h3><p>The brief, the audience and the single feeling the film must leave are decided before any model is opened.</p></div>
      <div class="card"><span class="icon-num">02</span><h3>Locked references</h3><p>Characters, products and brand systems are locked as references so every generation stays on-model.</p></div>
      <div class="card"><span class="icon-num">03</span><h3>Finished like a commercial</h3><p>Edit, grade, score and mix happen in Premiere, Resolve and After Effects, just as they would on a traditional spot.</p></div>
      <div class="card"><span class="icon-num systems">04</span><h3>Systems you own</h3><p>Every workflow lives in client accounts, with documentation and training, so the studio is never a dependency.</p></div>
      <div class="card"><span class="icon-num systems">05</span><h3>Measured speed</h3><p>About 60%% faster VFX and post turnaround and up to 3x production speed, used to give clients more iterations, not fewer hours of care.</p></div>
      <div class="card"><span class="icon-num">06</span><h3>Honest labels</h3><p>Spec work is labelled as spec, NDA work stays private, and AI use is disclosed the way each client and platform requires.</p></div>
    </div>
  </div>
</section>
<section class="section"><div class="wrap"><h2>About <em>FAQ</em></h2>[[FAQ]]
<p class="mt2"><a class="link-arrow cinema" href="%s" rel="me noopener" target="_blank">Connect with Josh on LinkedIn</a></p></div></section>
%s''' % (SITE['linkedin'], CTA)

BOOK = '''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="[[L:]]">Home</a> / Book</p>
    <h1>Book a 15-minute <em>discovery call.</em></h1>
    <p class="lede">Pick a time on the calendar, or send a project brief and Josh will reply within one business day. Either way you get a straight answer on fit, scope, price and timeline.</p>
    <p class="mt2">Prefer email? <a href="mailto:%s">%s</a></p>
  </div>
</section>
<section class="section">
  <div class="wrap book-grid">
    <div><h2 class="mb2" style="font-size:32px">Calendar</h2>%s</div>
    <div><h2 class="mb2" style="font-size:32px">Project brief</h2>%s</div>
  </div>
</section>''' % (SITE['email'], SITE['email'], cal_embed(760), brief_form())

NOT_FOUND = '''<section class="page-hero"><div class="wrap">
  <span class="eyebrow">404</span>
  <h1>That cut didn't make <em>the final edit.</em></h1>
  <p class="lede">The page you were looking for has moved or never existed.</p>
  <div class="btn-row mt2"><a class="btn btn-primary" href="[[L:]]">Back to home</a><a class="btn btn-ghost" href="[[L:work/]]">See the work</a></div>
</div></section>'''

PAGES = [
    dict(path='', title='Baez Studio | Cinematic AI Video & Custom AI Business Stacks',
         desc='Baez Studio pairs 15+ years of commercial editing with generative AI video and bespoke AI business workflows. Brand films from $1,500, AI stacks from $2,500. Ann Arbor, Fort Wayne, worldwide.',
         body=HOME, faqs=HOME_FAQS, ld=[SHOWREEL_LD], reel=True, preload=HERO_PRELOAD, priority='1.0'),
    dict(path='video-production/', title='Cinematic AI Video Production & Paid Social | Baez Studio',
         desc='Brand films, brand revivals, game cinematics and paid-social Hook Packs made with generative AI and finished by a 15-year commercial editor. From $1,500, 4K delivery in 5–21 days.',
         body=VIDEO, faqs=VIDEO_FAQS, reel=True, priority='0.9',
         ld=[svc_ld('Cinematic AI Video Production', 'Worldwide', 'https://baez.studio/video-production/', 'Brand films, revivals, lore cinematics and paid-social hook packs using generative AI compositing and Remotion.')],
         crumbs=[('Home', ''), ('Video Production', 'video-production/')]),
    dict(path='ai-business-stacks/', title='Custom AI Business Stacks & Workflow Automation | Baez Studio',
         desc='Bespoke AI workflows that turn one spreadsheet or CRM into lifecycle emails, newsletters, branded flyers and social posts. Audit from $750, builds $2,500–$18,000, 100% client-owned.',
         body=STACKS, faqs=STACK_FAQS, priority='0.9',
         ld=[svc_ld('Custom AI Business Stacks', 'Worldwide', 'https://baez.studio/ai-business-stacks/', 'Custom ChatGPT, Gemini and Claude workflows with Google Workspace, n8n and Make automation for email, newsletters, flyers and social publishing.')],
         crumbs=[('Home', ''), ('AI Business Stacks', 'ai-business-stacks/')]),
    dict(path='work/', title='Work & Case Studies | Baez Studio', desc='Selected AI brand films, spec ads, character work and AI business stack case studies by Baez Studio, with scene breakdowns and Josh Baez\'s role on each.',
         body=WORK, crumbs=[('Home', ''), ('Work', 'work/')], priority='0.8'),
    dict(path='work/showreel-2026/', title='Showreel 2026 | Baez Studio', desc='The Baez Studio 2026 showreel: 90 seconds of cinematic AI brand films, revivals, game cinematics and campaign spots, with a scene-by-scene breakdown.',
         body=CASE_SHOWREEL, reel=True, ld=[SHOWREEL_LD], crumbs=[('Home', ''), ('Work', 'work/'), ('Showreel 2026', 'work/showreel-2026/')]),
    dict(path='work/cellar-reserve-spec/', title='Cellar Reserve Spec Ad: Brief to 4K Master | Baez Studio', desc='Spec Ad Showcase: a premium wine spot shown from brief board to storyboard, generative compositing and graded 4K master.',
         body=CASE_CELLAR, crumbs=[('Home', ''), ('Work', 'work/'), ('Cellar Reserve', 'work/cellar-reserve-spec/')]),
    dict(path='work/fly-mascot/', title='Fly Mascot Character Animation | Baez Studio', desc='Character-consistent AI animation for Fly, the Baez Studio robot cat mascot: flight and wave loops for web and social.',
         body=CASE_FLY, ld=[FLY_LD], crumbs=[('Home', ''), ('Work', 'work/'), ('Fly mascot', 'work/fly-mascot/')]),
    dict(path='work/studio-content-engine/', title='Studio Content Engine: AI Business Stack Blueprint | Baez Studio', desc='Blueprint of the in-house AI stack that turns one Google Sheet into social posts, newsletter blocks and branded flyers with human approval.',
         body=CASE_STACK, crumbs=[('Home', ''), ('Work', 'work/'), ('Studio Content Engine', 'work/studio-content-engine/')]),
    dict(path='locations/', title='Service Areas: Ann Arbor, Fort Wayne & Worldwide | Baez Studio', desc='Baez Studio serves Ann Arbor, MI and Fort Wayne, IN in person and clients worldwide remotely, for cinematic AI video and custom AI business stacks.',
         body=LOC_HUB, crumbs=[('Home', ''), ('Service Areas', 'locations/')], priority='0.6'),
    dict(path='locations/ann-arbor/', title='AI Video & AI Automation in Ann Arbor, MI | Baez Studio', desc='Investor pitch films, technical explainers, Remotion product demos and AI sales-ops stacks for Ann Arbor startups, U-M spinouts and B2B SaaS teams.',
         body=ANN, faqs=ANN_FAQS, priority='0.7',
         ld=[svc_ld('AI video production and AI automation in Ann Arbor', {"@type": "City", "name": "Ann Arbor", "containedInPlace": {"@type": "State", "name": "Michigan"}}, 'https://baez.studio/locations/ann-arbor/', 'Pitch films, technical explainers, Remotion demos and AI sales-ops stacks for Ann Arbor startups and SaaS teams.')],
         crumbs=[('Home', ''), ('Service Areas', 'locations/'), ('Ann Arbor, MI', 'locations/ann-arbor/')]),
    dict(path='locations/fort-wayne/', title='AI Video & Workflow Automation in Fort Wayne, IN | Baez Studio', desc='Product and recruiting films, AI post-production overflow and workflow automation for Fort Wayne and Northeast Indiana manufacturers, healthcare, retail and agencies.',
         body=FW, faqs=FW_FAQS, priority='0.7',
         ld=[svc_ld('AI video production and workflow automation in Fort Wayne', {"@type": "City", "name": "Fort Wayne", "containedInPlace": {"@type": "State", "name": "Indiana"}}, 'https://baez.studio/locations/fort-wayne/', 'Recruiting and product films, agency overflow post-production and AI workflow automation for Northeast Indiana businesses.')],
         crumbs=[('Home', ''), ('Service Areas', 'locations/'), ('Fort Wayne, IN', 'locations/fort-wayne/')]),
    dict(path='about/', title='About Josh Baez, Founder & Creative Director | Baez Studio', desc='Josh Baez: creative producer, performance video editor and AI production systems architect with 15+ years of commercial post since 2008. Point Park University, Beam Suntory.',
         body=ABOUT, faqs=ABOUT_FAQS, priority='0.7',
         ld=[{"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": {"@id": "https://baez.studio/#josh"}}],
         crumbs=[('Home', ''), ('About', 'about/')]),
    dict(path='book/', title='Book a 15-Minute Discovery Call | Baez Studio', desc='Book a free 15-minute discovery call with Josh Baez or send a project brief for cinematic AI video, a custom AI business stack, or both.',
         body=BOOK, crumbs=[('Home', ''), ('Book', 'book/')], priority='0.8'),
    dict(path='404', title='Page not found | Baez Studio', desc='This page does not exist.', body=NOT_FOUND, noindex=True, org=False),
]
