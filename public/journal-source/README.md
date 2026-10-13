# Tourette.fyi research journal

The existing public domain remains on Cloudflare Worker tourette-fyi. The replacement journal is prepared in this real source checkout. Production deployment is held for parent review. Shared voting is disabled by feedback-config.json and the proposed service's feature gates. No public privacy contact or provider logging/backup/retention review is complete yet.

## Source and preview

Buildless source: dist/index.html, journal.css, journal.js, research-feed.json and feedback-config.json. worker.js retains HTTPS/www redirects and adds a GET-only /api/public-feed route. No DNS or Wrangler route configuration changed. The old survey assets remain unreferenced rather than deleting unrelated local work.

The journal includes six genuine repository-work entries dated October 8 through 13, primary-study notes with evidence types and dated repository access checks, opt-in reduced-motion-aware sketch animation, browser-supported user-triggered narration, six optional leisure/movement ideas and an unsent page-memory reflection. No free-text form, personal origin story, analytics, identifiers or health-feedback submission exists. No em dash appears in visible text.

No browser/app surface is connected to this delegated environment. Source and jsdom interaction checks can verify behavior; rendered desktop/mobile/200-400% zoom and physical keyboard/speech testing require the parent browser-capable executor before claiming they passed.

## Unattended daily publication

The current public GitHub main branch contains public/research-feed.json. The landing Worker reads only the fixed raw GitHub URL server-side, with a short cache and no credentials. The browser reads the same-origin /api/public-feed endpoint. Failed, malformed, oversized, future-dated or older content retains the saved edition with honest timestamp/status. There is no browser persistence or fake live execution indicator.

A cloud research task can update public/research-feed.json using the GitHub connector, so routine content publication does not require this computer to be awake or a new Wrangler deployment. The parent owns updating the existing daily automation after source readback verification. Each feed edit must reflect actual verified work and a true content-write updatedAt timestamp; lastResearchDate must be the latest verified research day. Preserve source/evidence type, limitations, and negative findings. Do not put personal stories or participant data in the feed.

Readback contract: fetch public/research-feed.json from dotjade/project-neurofreedom through the GitHub connector and anonymous raw GitHub HTTP, compare content to the committed source, and validate schema/date/order. After final deployment, also read https://tourette.fyi/api/public-feed and verify X-Journal-Source=repository and the expected updatedAt. Source readback before deployment does not prove the production Worker route is updated.

## Feedback service preparation

feedback-service/ is a separate identity-free Sites Worker ESM preparation with a D1 DB binding, schema-only migrations, HTTP/SQL tests and packaging instructions. It is not registered, provisioned or deployed. The retained old survey Sites identity is unchanged. A public API origin, privacy contact, hosting logs/backup review, and verified hosted expiry schedule remain dependencies. Application-level 30-day deletion must not be described as instant deletion from provider backups. Until these gates are complete, there are no active vote controls and no fabricated counts.

Publication still uses the existing authenticated Wrangler workflow. No credentials, public writer secret, paid resource or persistent permission expansion are part of this source.
