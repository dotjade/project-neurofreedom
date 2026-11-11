# November 11 public-link and activity review

## Result

The bounded 46-URL research/feed pass found 38 retrievable or identity-checked targets and eight access-limited targets. No research citation was confirmed broken. Two supplemental requests verified the live runtime and reconfirmed the linked favicon's HTTP 404. The six approved activity records are unchanged, rest and skipping remain equal choices, and collection remains disabled.

The recommended next catalog selection is `familiar-route`, following November 10's `hand-at-ease`. This is an editorial rotation of an existing ordinary optional activity, not a new intervention or clinical result.

## Actual method and scope

Fresh requests ran from `2026-11-11T03:15:06.957550+00:00` to `2026-11-11T03:15:43.112216+00:00`. Each URL received an ordinary anonymous curl GET with redirects, a 30-second timeout and at most five redirects. Five workers ran concurrently. No credentials, custom user agent, security override, challenge solution, sign-in or bypass was used. No denied request was retried by another route.

The pass covered all 24 current timeline records and three findings, the six static fallback research records and nine other homepage research citations, homepage, production API, anonymous raw feed, and feedback configuration. Homepage research links were cross-checked against the local homepage source; repository navigation and contribution links were outside this pass. Two supplemental checks covered journal.js and favicon.svg. The [request ledger](../../public/link-checks/2026-11-11.json) records request timestamps, response statuses, final URLs, identity checks and limits. Previous dates supplied scope and comparison context only; their results were not copied as current observations.

## Link findings

- Thirty GitHub research records returned HTTP 200 with their expected repository path and a rendered markdown marker.
- CDC, MedlinePlus Genetics and the ONLINE-TICS publisher page returned HTTP 200 with expected identity text.
- Ivanova's primary PDF returned HTTP 200 with a PDF signature. Extracted text contained DOI `10.1186/s44247-026-00284-7`. Temporary full-text files were deleted after the identity check; no paper is included in the deliverables.
- Isaacs PMC10863457 and six PubMed introduction citations (21955933, 16520330, 17987065, 25264251, 25044024 and 26041822) returned HTTP 203 access-limited pages. Target article content was not verified.
- Pappert's publisher DOI returned HTTP 403 with a “Just a moment...” challenge page. This does not establish that the source is broken.
- Homepage, public-feed API, raw feed and feedback configuration returned HTTP 200.
- Supplemental journal.js returned HTTP 200 and matched local source bytes. The linked favicon.svg returned empty HTTP 404. This is a missing icon asset, not a broken research citation; no fix was made.

Keep canonical primary links. Supported November 11 finding metadata is:

- Isaacs: “Direct HTTP 203 access-limited response; article content not verified in this pass”.
- Pappert: “Publisher HTTP 403 challenge; source not established broken in this pass”.
- Ivanova: “Primary PDF retrieved with HTTP 200; DOI identity verified”.

These are access/identity observations, not independent revalidation of scientific claims.

## Prepublication baseline

The production API and anonymous raw feed both matched local public/research-feed.json bytes, SHA-256 `9b577218a18787327b0cb90aa7e3b10980b6e4480559eaee17a7cec213fa837f`. The API returned `X-Journal-Source: repository`. Both represented updatedAt `2026-11-10T03:28:59Z`, lastResearchDate and activityEditionDate `2026-11-10`, and featuredActivityId `hand-at-ease`. These observations precede November 11 publication and do not prove a later edition is live.

The live homepage and JavaScript matched local journal-source bytes. The homepage contains the Tourette introduction anchor and no form. No report for the as-yet-unpublished November 11 edition was fetched in this review; verify its new link after publication.

## Activity and collection review

All six feed activity objects exactly match the saved approved catalog: hand-at-ease, familiar-route, notice-one-thing, music-or-silence, small-silly-mark and rest-or-leave. Each retains its seated, standing and rest alternative. Source rendering explicitly says “Optional. Rest or skip equally. Stop if uncomfortable.” No food field, exertion target, breath holding, suppression task, timer, streak or new activity was added. These cards are ordinary optional leisure/movement ideas, not established tic or ADHD treatments. This preservation check is not clinical safety certification.

Feed feedback remains enabled=false with sampleSize zero and empty aggregates/trend. Live and local feedback-config.json both contain enabled=false, apiOrigin=null and verifiedAt=null. Source inspection confirms setupVotes returns at that gate before summary requests or vote controls. No live vote or write request was made, and no dynamic vote execution test is claimed for this pass.

The reviewed homepage and runtime have no form or localStorage, sessionStorage, sendBeacon or document.cookie use. Reflection is page-memory-only, is cleared on pagehide and restored pageshow, and is excluded from narration. Hosting-request metadata remains disclosed. No personal/family story, participant data, treatment advice or collection feature was introduced by this review.

## Limits and handoff

This is a bounded HTTP/source review, not an exhaustive crawl, rendered browser/network audit, accessibility certification or real-device test. No fresh mobile/zoom, physical keyboard/touch or speech test was performed. The dated static fallback and static next-question section are unchanged; a feed edit cannot refresh those assets. The favicon issue is also outside this daily feed-only change.

Only this review and the November 11 request ledger were written by this review task. No runtime, activity, feed, deployment or external-state change was made. After publication, separately verify the new feed bytes, dated fields, repository-source header and new report URL after the cache interval.
