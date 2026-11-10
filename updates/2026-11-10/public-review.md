# November 10 public-feed and homepage audit

## Result

The 46-URL research/feed pass found 38 retrievable or identity-checked targets and eight access-limited targets, with no confirmed broken research source. The six approved optional activities are unchanged and collection remains disabled. A separate supplemental asset pass found the homepage's linked favicon missing (HTTP 404); it is not a browser-visible research citation. No repository, site-source, deployment or external-state changes were made.

## Source and production baseline

Before and after connector branch checks returned main `095c568b21ba8171867c7324f24548d0ee8617bc`, the November 9 publication-verification commit. Eleven exact-head connector files were saved outside the repository. All materialized files match their connector Git blob SHA, with SHA-256 and source URLs in `source-ledger.json`. Required README, protocol, current/recent STATUS, journal-source README and publication workflow were reviewed before the audit.

Connector feed blob `5df6d9c650eb4356a689d9fe8bf4dab16de9d380`, anonymous raw main feed, production API and live saved feed agree byte-for-byte. Feed SHA-256 is `78b78b7618c9aef03d76f10f501b841667dca697888aadfcd55b2fea5e87a84b`. The production API returned HTTP 200 and `X-Journal-Source: repository` at 03:27:27 UTC on November 10.

The baseline remains the November 9 daily edition: updatedAt `2026-11-09T02:58:10Z`, lastResearchDate and activityEditionDate `2026-11-09`, featuredActivityId `rest-or-leave`. It has schema version 1, 24 descending timeline entries, three findings, six distinct activities, no future timeline dates and no em dash. The exact live JavaScript validator accepts this feed. Live homepage, JavaScript and feedback configuration match the exact-head source bytes.

The Worker source reads only the fixed public GitHub feed without credentials, admits GET/HEAD for the public-feed route and uses a 120-second cache with saved-feed fallback. No write-method request, voting, participant collection, outreach or sign-in occurred.

## Activity and collection checks

All six records exactly match the approved saved-source catalog: hand-at-ease, familiar-route, notice-one-thing, music-or-silence, small-silly-mark and rest-or-leave. Seated, supported, comfortable and rest/skip alternatives remain. No new physical or food activity, food field, exertion target, breath hold, suppression task, timer or streak was introduced. The existing ordinary leisure/movement cards are not established tic or ADHD treatments. This is a content-preservation check, not clinical safety certification.

Feed feedback is disabled, sampleSize is zero, and aggregates/trend are empty. Live feedback-config.json remains enabled=false, apiOrigin=null and verifiedAt=null. Isolated execution of the exact live setupVotes function with that configuration made only the mocked configuration read and returned without vote controls, summary calls or votes. No third-party request was sent by the mock test.

The page has no form. Live JavaScript has no localStorage, sessionStorage, sendBeacon or document.cookie use. Reflection remains page-memory-only, clears on pagehide and restored pageshow, and is excluded from narration. Hosting-request metadata is disclosed. This is not an end-to-end browser network audit.

## Bounded research and feed link pass

Original checks ran from `2026-11-10T03:26:55.752574+00:00` to `2026-11-10T03:27:34.907072+00:00`. Ordinary anonymous curl GETs followed redirects with bounded timeouts and five workers, without credentials, a custom user agent, security override or bypass. The 46 URLs cover all 24 current timeline records, three findings, six static fallback research records, nine other homepage research links, homepage, production API, anonymous raw feed and feedback configuration. Original per-request timestamps, HTTP statuses, final URLs and identity checks are in `link-checks-2026-11-10.json`.

- Thirty GitHub research records returned HTTP 200 with the expected repository path and rendered-article marker.
- CDC, MedlinePlus Genetics and the ONLINE-TICS publisher page returned HTTP 200 with expected identity text.
- Ivanova's primary PDF returned HTTP 200 with a PDF signature and DOI `10.1186/s44247-026-00284-7` verified in extracted text. The temporary full-text copy was deleted; no paper copy is in this artifact package.
- Isaacs PMC10863457 and six PubMed introduction citations (21955933, 16520330, 17987065, 25264251, 25044024 and 26041822) returned HTTP 203 access-limited pages. Their target article content was not verified.
- Pappert's publisher DOI `10.1212/01.WNL.0000086370.10186.7C` returned HTTP 403 with a challenge page. It is not established broken. No challenge or access restriction was bypassed.
- Homepage, production API, raw feed and feedback configuration returned HTTP 200.

Keep these canonical primary URLs. Access limits are not dead-source findings. This pass does not independently revalidate study claims.

## Supplemental navigation, assets and anchors

Five supplementary ordinary GETs started at 03:27:32 UTC, recorded separately in `supplemental-link-checks.json`:

- Repository navigation: HTTP 200 and expected project identity.
- Contribution link: HTTP 200 after redirect to the expected GitHub sign-in page. No form submission or sign-in was attempted.
- QR download: HTTP 200, SVG content. No fresh QR decoding was performed.
- Stylesheet: HTTP 200, CSS content.
- `https://tourette.fyi/favicon.svg`: empty HTTP 404. Exact live homepage/source includes `href="favicon.svg"`; the exact Git tree contains no favicon path. This confirms a missing linked icon asset in the checked edition. It is separate from the 46 research/feed URLs and is not a broken browser-visible research citation. No fix was attempted.

Same-page #main and #what-is-tourette targets exist in the live homepage source. Asset HTTP snapshots separately verify live journal.js, research-feed.json and feedback-config.json.

## Publication integration and limits

1. This is the prepublication November 9 baseline. After publishing November 10 work, verify exact new connector/raw/live feed bytes, repository-source header and new report URLs after the cache interval.
2. The three finding checks support checkedAt `2026-11-10`; their observed states are unchanged: Isaacs, "Direct HTTP 203 access-limited response; article content not verified in this pass"; Pappert, "Publisher HTTP 403 challenge; source not established broken in this pass"; Ivanova, "Primary PDF retrieved with HTTP 200; DOI identity verified". No feed edit was made here.
3. The feed is at its 24-entry limit. A new feed entry must displace the oldest feed item while preserving its permanent research record.
4. Known static limitations persist: no-JavaScript research/activity copy is dated October 13 and the static next-question section still points to ONLINE-TICS. Feed-only changes cannot update those assets. The newly checked missing favicon is likewise an asset issue. No site-source changes are proposed for this daily research run.
5. No fresh rendered desktop/mobile, zoom, keyboard/touch, real-device narration, accessibility or clinical safety test was performed. No certification or exhaustive crawl is claimed.

## Saved check records

The [research link ledger](../../public/link-checks/2026-11-10.json), [supplemental resource ledger](supplemental-link-checks.json), [feed safety checks](feed-safety-checks.json), [static checks](static-source-checks.json), [asset observations](asset-http-checks.json) and [source provenance](source-ledger.json) preserve the actual checks. This review predates the new feed; publication verification is separate.
