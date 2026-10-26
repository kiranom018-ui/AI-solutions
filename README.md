# James AI Solutions website
Static HTML/CSS/JavaScript website for James AI Solutions. No server, paid API, framework or package installation is required. This repository contains public website source only.

## Recommended free hosting
Cloudflare Pages, connected to this GitHub repository. Production branch: main. Build command: `python3 build.py`. Output directory: `dist`. Root directory: repository root. Set `SITE_URL` to the exact verified production origin after the Pages project is created, then redeploy. Without SITE_URL the review build is noindex and robots disallows crawling. This avoids publishing guessed canonical addresses.

GitHub Pages is technically capable of serving these static files; current GitHub limits restrict sites primarily facilitating commercial transactions. Use GitHub as source control and Cloudflare as the business host. No Pages deployment workflow is enabled here.

## Local review
Run `python3 build.py`, then `python3 -m http.server 8906 --directory dist --bind 127.0.0.1`. Set SITE_URL only for a confirmed production domain. Run `python3 check_site.py` to validate links, assets, headings and structured data.

## Domain
No domain is purchased or configured. Do not add a CNAME for an unowned domain. After purchase, add the exact domain through Cloudflare Pages custom domains, follow the returned DNS instructions, verify HTTPS, set SITE_URL and redeploy. Redirect the alternate hostname to the canonical hostname. Submit the sitemap to Search Console after verifying ownership. No guaranteed indexing or ranking.

## Privacy and service scope
The form prepares a WhatsApp message or downloads a text brief. It does not store leads, send emails or collect payment. Existing company WhatsApp route is reused; confirm phone control and business payment details before outreach. No internal plans, customer files, prospect lists, credentials or revenue targets belong in this public repository.

## Sources checked 26 October 2026
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- https://developers.cloudflare.com/pages/platform/limits/
- https://developers.google.com/search/docs/fundamentals/get-started-developers
