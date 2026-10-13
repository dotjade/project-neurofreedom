# Optional activity preference counters

Prepared for Sites Worker ESM with D1 binding `DB`. No project identity, credentials, public API origin, storage resource or deployment has been created by this source preparation. The old survey Sites identity is retained separately and is not repurposed or made public.

## Data boundary

Two tables contain only UTC day, allowlisted activity ID, and integer vote count. There are no per-person rows, user IDs, ages, diagnoses, health outcomes, IPs, individual timestamps, cookies, fingerprinting or free-text comments. Browser reflection is never included in the payload. Providers can still process request metadata and may inject authenticated identity headers; the application ignores them. Hosted logging practices remain unverified. Do not describe this as entirely anonymous.

Counts mean votes, not unique people or people helped. The service does not reliably exclude repeat or bot votes. Caps are 1,000 per activity/day and 2,000 globally/day. Without identifiers these are global safety limits, not per-person rate limits. An adversarial client can forge Origin and the request header; those checks protect ordinary browser cross-origin requests, not authenticate people.

The sole vote payload is `{ "activityId": "notice-one-thing" }` or one of the six fixed activity IDs in worker/index.js. Extra fields are rejected. Bodies are read with a 96-byte streaming limit. POST requires the exact `https://tourette.fyi` Origin, JSON Content-Type and `X-Tourette-Vote: v1`. CORS allows only that origin, no credentials, the exact POST method and two request headers. No client writer secret exists.

## Retention gate

Reads and writes delete aggregate days older than the current UTC day minus 29 days. `scheduled` performs the same expiry deletion; `/api/cleanup` is an unauthenticated, expiry-only cleanup route for a platform-supported schedule. It cannot remove in-window rows or create data.

Request-triggered deletion alone does not guarantee physical expiry while nobody visits. The host must attach and verify a recurring cleanup invocation, ideally at each UTC day boundary, before setting `RETENTION_SCHEDULE_CONFIRMED=true`. The Sites hosting manifest does not document cron-trigger configuration. Do not invent a `cron` manifest field or silently promise enforced expiry. The parent must verify whether native Sites automation or a supported hosted scheduled hook can invoke cleanup independently of the desktop. If no suitable schedule can be verified, keep voting off. Provider backups and platform log retention are outside this application cleanup and require truthful disclosure.

Voting and summary endpoints fail closed unless both `PUBLIC_VOTING_ENABLED=true` and `RETENTION_SCHEDULE_CONFIRMED=true` are configured using supported native runtime tools. These values are feature gates, not secrets or proof that a schedule exists.

## Packaging and parent publication checklist

1. Confirm the dedicated public API publication scope, provider logging limits, and hosted retention schedule. Do not switch the landing page's hosting or DNS.
2. Register this separate backend through native Sites tools only if approved. Persist the returned project ID with the supported helper. Never copy the old survey ID here.
3. Keep `.openai/hosting.json` with `d1: "DB"`, `r2: null`; no static binding. Initial SQL is schema-only in `drizzle/`; append later migrations without rewriting applied history.
4. Run `node scripts/build.mjs`. The deterministic artifact contains `dist/server/index.js`, `.openai/hosting.json`, and `.openai/drizzle` migrations, following the Sites starter's migration packaging convention.
5. Open/synchronize/package with the supported Sites source helper and a short-lived source credential through stdin. Use the exact returned commit/archive for native save and deploy. The current source is a preparation; hosted migration and D1 batch behavior still need verification.
6. Publish only this API origin with the explicitly intended public access. Test allowed/disallowed CORS, vote/summary readback, caps, cleanup and anonymous access without cookies. Do not enter health or personal data during testing.
7. Only after verification, put the actual API origin and verification timestamp in the landing page's feedback-config.json, and allow exactly that origin in CSP connect-src. Never add a wildcard. Then enable the parent-approved service gates and deploy the landing page through its existing Wrangler route.

No active vote button appears while configuration is disabled or the API read check fails. No fake votes are seeded. A successful initial readback must be recorded before calling storage live. The parent owns the automation update and final deployment decision.

Collection remains disabled pending the public privacy contact and hosting review. Application-level cleanup must not be described as instant deletion of all copies: D1 provider backups may retain deleted content for 7 or 30 days depending on the plan, which must be checked before launch.
