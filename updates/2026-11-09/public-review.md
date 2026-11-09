# Public feed, approved optional activities and bounded link check

Checked 9 November 2026. This was a read-only review: no repository edit, publication, vote, participant collection or other external state change.

## Verified source and live baseline

- GitHub connector branch reads before and after the review returned main `a68355a22f7de6e694ac4df29ad670983dd6c68f`, the November 8 weekly publication-verification commit. Exact-head connector copies of README, RESEARCH_PROTOCOL, STATUS, the latest daily and weekly reports, public/UPDATE_WORKFLOW and journal source files were materialized outside the repository. All 13 materialized files match their connector Git blob SHA; SHA-256 and source URLs are in `public-source-ledger.json`.
- The latest plan is the bounded public-aggregate measurement-anchor/invariance audit, capped at six primary reports and 90 minutes, not a repeat of the completed H18 simulation or closed source map. This public-feed review does not perform that scientific audit.
- Feed blob `1b602b8605ee8d6f65309baf0f3fc7fc8983cc43`, anonymous raw main feed, production API and live saved feed agree byte-for-byte. Feed SHA-256: `639c09b9e1718d5694bd557b3fdde7e1f88339e87ea7a9e861c261dbb108ccb3`.
- Production API returned HTTP 200 and `X-Journal-Source: repository`. The verified live baseline is the November 8 daily edition: updatedAt `2026-11-08T03:14:13Z`, lastResearchDate and activityEditionDate `2026-11-08`, featuredActivityId `small-silly-mark`.
- Schema version 1, 24 descending timeline entries, three findings, six distinct approved activities, no future timeline dates and no feed em dash. The exact live JavaScript `validFeed` function accepts the feed.
- Live homepage, JavaScript and feedback configuration all returned HTTP 200 and exactly match the corresponding source bytes at the verified head. The introduction anchor exists, and the HTML has no form. This is HTTP/source inspection, not rendered-browser or accessibility verification.
- The source Worker reads the fixed public GitHub feed without credentials, with a 120-second cache. The route admits GET/HEAD and has a saved-feed fallback. No write-method or voting request was sent during this review.

## Optional activity and collection review

All six activity records exactly match the approved saved-source catalog: hand-at-ease, familiar-route, notice-one-thing, music-or-silence, small-silly-mark and rest-or-leave. Each retains seated, standing and rest alternatives, usual supports, comfort-based choices and permission to imagine, skip or leave. No exertion targets, breath holds, suppression tasks, timers, streaks or food-risk activities were introduced. Public copy identifies the cards as ordinary leisure rather than proven tic/ADHD treatments, says users need not hold back tics, and says to stop if uncomfortable. The dated catalog selection is not new clinical evidence. This content check is not clinical safety certification.

Feed feedback remains disabled, sampleSize is zero, and aggregates/trend are empty. Live feedback-config.json has enabled=false, apiOrigin=null and verifiedAt=null. An isolated execution of the exact live `setupVotes` function with this configuration made only the mocked configuration read and returned without rendering vote controls or attempting summary/vote calls. This was a source-level gate test, not a live browser network audit; it sent no actual votes or third-party requests.

Reflection remains page-memory-only, clears on pagehide and restored pageshow, and is excluded from narration. The exact live JavaScript contains no localStorage, sessionStorage, sendBeacon or document.cookie use. The page discloses ordinary hosting-request metadata. No health-outcome collection, comments or voting were enabled.

## Bounded displayed links: 46 URLs

Checks ran from 02:39:43 to 02:40:27 UTC on November 9. The pass covered all 24 current timeline research links, three finding links, six static fallback research links, nine other homepage research links, homepage, production API, anonymous raw feed and feedback configuration. General repository navigation, the contribution form, local QR asset and same-page anchors were outside this link pass. Ordinary anonymous curl GETs followed redirects without credentials, a custom user agent, security override or bypass. Each URL has a timestamp, status, final URL and identity check in `../../public/link-checks/2026-11-09.json`.

- Thirty GitHub research records returned HTTP 200 with the expected repository path and rendered article marker.
- CDC, MedlinePlus Genetics and the ONLINE-TICS publisher page returned HTTP 200 with expected identity text.
- The Ivanova primary PDF returned HTTP 200 with a PDF signature and DOI `10.1186/s44247-026-00284-7` verified in extracted text. The temporary paper copy was deleted; no full-text paper is retained in the artifact package.
- Isaacs PMC10863457 and six PubMed introduction citations (21955933, 16520330, 17987065, 25264251, 25044024 and 26041822) returned HTTP 203 access-limited responses. Their target article content was not verified by this pass.
- Pappert publisher DOI `10.1212/01.WNL.0000086370.10186.7C` returned HTTP 403 with a challenge page. The source is not established broken. No protection was bypassed and no alternate institutional copy was checked.
- Homepage, production API, raw feed and feedback configuration returned HTTP 200.

Total: 38 retrievable or expected-target checks satisfied, eight access-limited endpoints, no 404/410 and no confirmed broken link. An access-limited endpoint is not a dead source. Retain the canonical source URLs. This availability check does not independently revalidate scientific claims in those studies.

## Integration notes and remaining limits

1. The three findings currently display November 8 review dates. This pass supports November 9 checkedAt values. Precise states remain: Isaacs, "Direct HTTP 203 access-limited response; article content not verified in this pass"; Pappert, "Publisher HTTP 403 challenge; source not established broken in this pass"; Ivanova, "Primary PDF retrieved with HTTP 200; DOI identity verified". These suggestions have not been written to the repository or live feed.
2. The feed is at the renderer's 24-entry limit. Add a new entry only by dropping the oldest feed item, while retaining its permanent research record.
3. The no-JavaScript static fallback still displays the October 13 research/activity edition and older finding review dates. The static next-question section still refers to ONLINE-TICS rather than the latest STATUS plan. These are known source limitations, not new feed regressions. A feed-only update cannot change them. Live saved JSON is current and matches the November 8 repository edition.
4. This review verifies the November 8 baseline only. After November 9 publication, recheck exact new source/live feed bytes, repository-source header, new report URLs, schema and dates after the cache interval.
5. No fresh rendered desktop/mobile, zoom, physical keyboard, touch or real-device narration test was performed. No accessibility certification, exhaustive browser-network audit, exhaustive link crawl or clinical safety certification is claimed.

## Original review-package map

- `../../public/link-checks/2026-11-09.json`: 46 timestamped URL checks and identity flags.
- `public-safety-checks.json`: schema/date/catalog checks, source/live equality and disabled-collection/voting checks.
- `public-source-ledger.json`: exact-head document/source hashes, Git blob matches and URLs.
- `remote-main.json` and `final-remote-main.json`: before/after GitHub branch readbacks.
- `connector-feed.json`, `homepage.html`, `live_journal.js`, `live_research-feed.json` and `live_feedback-config.json`: connector/live snapshots.
- `asset-http-checks.json`, `check_links.py` and `check_safety.cjs`: asset statuses and reproducible checks.
- `artifact-ledger.json`: SHA-256 and byte lengths for all final review files other than the ledger itself.

The reviewer prepared the original package outside the repository and made no repository edits. Publication archives this report, the dated URL ledger, source ledger and safety checks. Other diagnostic snapshots and scripts listed above describe the original working package and are not included in this compact permanent subset. No new verification is implied by archival.
