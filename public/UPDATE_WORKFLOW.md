# Public journal update workflow

Verified publication: 13 October 2026. https://tourette.fyi/ replaces the survey. The research repository is public. Do not publish personal or family information, participant records, secrets, private community material or unlicensed full-text papers.

## Verified route
The existing Cloudflare Worker serves the journal. Its GET-only /api/public-feed route reads public/research-feed.json from this repository without credentials. The initial source write and anonymous readback were verified, followed by production readback showing the repository edition. Routine feed changes do not require a desktop or a Worker redeployment.

Published Worker version: 946a1e9c-42bb-4490-bede-feb44766082a.
Published source snapshot: f0a478f2d0120486d07ea12f67bcd85cd5db63da.
The source snapshot is under public/journal-source/.

## Each daily publication
1. Complete the bounded research task under RESEARCH_PROTOCOL.md and the latest plan. Update evidence records before writing the public summary.
2. Fetch the latest public/research-feed.json and preserve unrelated changes. Use its current blob SHA for the update.
3. Keep schemaVersion 1, honest updatedAt, lastResearchDate and ordered timeline entries. The current renderer accepts at most 24 timeline entries, 12 findings and six distinct allowlisted activities. Keep older work in its permanent research files rather than exceeding these limits.
4. Explicitly select featuredActivityId from the existing catalog and set activityEditionDate to the date of that selection. A new activity selection is not new clinical evidence. The browser does not invent new research or automatically update these fields.
5. Record no-change scans honestly. Do not imply a breakthrough, continuous execution, patient benefit or a cure. Keep summaries short and evidence types clear. No em dashes in public page copy.
6. Verify displayed source links in a bounded pass. Record check date, reachable or limited-access status, and any replacement primary link. A bot block is not proof a source is dead.
7. Commit through the authorized GitHub connector. Read back the file, then the production /api/public-feed route after the short cache. Verify updatedAt and the repository-source indication. If publication fails, retain the last verified edition and report the exact blocker.
8. The static next-question section is currently part of index.html. Keep its question aligned with the plan when redeploying; a feed-only update does not change that section.

## Safety and feedback
Only ordinary optional activities are in the launch catalog. Rest, alternatives and skipping are equal choices. No evidence establishes these exact cards as tic or ADHD treatments. Do not add exertion targets, breath holding, suppression, timers, streaks or food-risk activities without appropriate review.

Shared voting is OFF. Page-local reflection is not submitted or stored. The prepared Sites/D1 service has not been provisioned or published. Enabling it requires a public project contact, an accurate privacy notice, provider logging/backup review, a verified public API and retention/integration tests. Aggregate votes would reflect preferences, not unique people or treatment effects. No public comments or health-outcome collection is authorized by this publication workflow.

## Verification limits
The desktop source reported 22 passing journal checks plus backend preparation tests. Production assets matched the committed source. Parent cloud-browser review verified the rendered desktop page, live repository edition and keyboard expansion of an activity alternative. Browser narration had no available voices in that cloud browser and correctly showed an unavailable state. Real-device narration, mobile viewport and 200-400 percent zoom have not been independently verified; no WCAG certification is claimed.
