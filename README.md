# James AI Solutions — maintained company website

This repository is the single maintained source for the company website. Canonical company domain: https://jamesaisolutions.com/. Cloudflare Pages project: james-ai-solutions. GitHub source: kiranom018-ui/AI-solutions.

## Structure
- site/: public HTML, CSS, JavaScript, favicon and verification metadata.
- build.py: copies source to dist/ and emits canonical metadata, organization schema, robots.txt and sitemap.xml.
- check_site.py: validates page titles, headings, local links, fragment targets and schema syntax.

## Build and verify
`SITE_URL=https://jamesaisolutions.com python3 build.py`
`python3 check_site.py`
`node --check site/app.js`

For local review: `python3 -m http.server 8906 --directory dist --bind 127.0.0.1`.
Source files remain editable without cloud APIs or a framework installation. Review builds without SITE_URL are noindex. Dist is generated and not a second source tree.

## Deployment
The live project uses Cloudflare Pages Direct Upload. Package the contents of dist/ at ZIP root, then upload a new Production deployment through the existing project. GitHub commits do not automatically deploy. The connected Cloudflare GitHub account differs from this repository owner. A native Git integration would require a separate project; alternatively a scoped CI upload can be configured after credential approval. Do not invent credentials or extract browser sessions.

## Design and behaviour
Dark charcoal, warm brown, ember red; lightweight canvas orbital sculpture, pointer-responsive cards, keyboard-operated studio tabs, service selector and reduced-motion/pause support. There are no third-party JavaScript libraries. Illustrative examples are labelled and do not claim customer outcomes.

The enquiry form prepares a WhatsApp draft or downloads a text brief. It does not store leads or collect payment. Email routing status and outbound-mail acceptance are recorded separately in the private launch operations files. Phone: +91 90190 01934, reused from the founder's company source. No prospect lists, internal plans, credentials or customer data belong in this public repository.

## Retired copies
The old local brochure, company-site source and first sales site are archived in the founder's Google Drive under JAMES-Startup/Archive/Retired-Websites-2026-10-26. The obsolete james-company-website Docker container is stopped and automatic restart is disabled. Business applications remain separate.

## Verification
Production release evidence, DNS/email status, screenshots and the dated source backup are maintained in the private Google Drive launch folder. Google Search Console verification metadata is public by design. Do not remove it after ownership verification.
