# Public feed, optional activities and bounded research-link check

Checked 7 November 2026. Read-only review; no repository edits or external state changes.

## Verified baseline

- Remote main was `fbe540dd2552c07526418b407b1383be0a06a91b` at the first and final `git ls-remote` checks. Required README, RESEARCH_PROTOCOL, STATUS and public/journal-source/README were fetched from that exact commit and matched the November 6 local snapshot. The current next task is H18 randomized mechanism/component/generalization evidence, not repeating the closed H13 audit.
- GitHub connector feed blob: `675af77b868c24d2a1b1311475bb166f8f42dca4`. Connector, exact-commit raw source, branch raw source, production API and live saved feed agree byte-for-byte. SHA-256: `77e11ee7e606051a151242e5678572b95abf17702e9c49a59ec34643ffb894c4`.
- Production API returned HTTP 200 at 03:07:06 UTC with `X-Journal-Source: repository`. The baseline remains the November 6 edition: `updatedAt=2026-11-06T03:03:29Z`, `lastResearchDate=2026-11-06`, `activityEditionDate=2026-11-06`, `featuredActivityId=notice-one-thing`.
- Schema version 1, 24 descending timeline entries, three findings, six unique approved activities, no future timeline dates and no feed em dash. The exact production JavaScript `validFeed` function accepts the feed.
- Live homepage and JavaScript return HTTP 200 and exactly match exact-head source bytes. The introduction anchor exists and the HTML has no form. This is HTTP/source inspection, not rendered-browser or accessibility verification.

## Optional activity and collection review

All six catalog records exactly match the saved approved catalog: hand-at-ease, familiar-route, notice-one-thing, music-or-silence, small-silly-mark and rest-or-leave. Each retains seated, standing and rest alternatives, ordinary supports, comfort-based choice, imagining or skipping. There are no exertion targets, breath holds, suppression tasks, timers, streaks or food activities. The public wording states these are ordinary leisure ideas rather than proven tic/ADHD treatments, users do not need to hold back tics, and they should stop if uncomfortable. Selection is explicitly a fixed-catalog choice, not new research or a clinical recommendation. This content review is not clinical safety certification.

Feed feedback is disabled, sampleSize is zero, and aggregates/trend are empty. Live feedback-config.json returns HTTP 200 with enabled=false, apiOrigin=null and verifiedAt=null. Exact live JavaScript gates vote controls on all three values; no vote or summary request was made. Reflection is page-memory-only, clears on pagehide, and the source contains no localStorage, sessionStorage, sendBeacon or document.cookie. The page discloses ordinary hosting-request metadata. No health-outcome collection or vote controls were activated. This is not a fresh end-to-end browser network audit.

## Bounded links: 46 URLs, 03:06:25-03:07:16 UTC

Checked all 24 timeline research links, three finding links, six static fallback research links, nine other homepage research links, homepage, production API, raw feed and feedback configuration. Ordinary anonymous curl GETs followed redirects without credentials, custom user agent, security override or bypass.

- Thirty GitHub research records returned HTTP 200 with expected repository path and rendered article marker.
- CDC, MedlinePlus Genetics and ONLINE-TICS publisher pages returned HTTP 200 with expected identity text.
- Ivanova primary PDF returned HTTP 200 with PDF signature and DOI 10.1186/s44247-026-00284-7 verified in extracted text.
- Isaacs PMC10863457 and six PubMed introduction citations (21955933, 16520330, 17987065, 25264251, 25044024, 26041822) returned HTTP 203 challenge/access-limited responses. Their target content was not verified in this pass.
- Pappert publisher DOI 10.1212/01.WNL.0000086370.10186.7C returned HTTP 403 with a bot/access challenge. This is not established broken. No alternate institutional copy was checked.
- Homepage, production API, anonymous raw feed and feedback config returned HTTP 200.

Total: 38 retrievable/identity-confirmed endpoints; eight access-limited endpoints. No 404/410 or confirmed broken link. Preserve canonical sources and label access challenges honestly.

## Integration notes

1. All three findings currently display November 6 checks. Today's actual pass supports November 7 checkedAt values with the same route-specific states: Isaacs HTTP 203 target-unverified; Pappert publisher HTTP 403 challenge; Ivanova primary PDF HTTP 200 DOI-confirmed. No scientific claims were revalidated merely by checking links.
2. Feed remains at its 24-entry limit. When adding a new entry, drop only the oldest feed item and preserve its permanent research record.
3. The static no-JavaScript fallback remains dated October 13, and the static next-question text remains ONLINE-TICS despite the current STATUS plan. These are known source limitations, not new feed regressions. A feed-only update cannot change them.
4. This review verifies the November 6 baseline only. Recheck exact source/production bytes and new report links after any November 7 publication.
5. No fresh rendered/mobile/zoom/physical-keyboard/narration check or accessibility certification is claimed.

## Saved artifacts

- [Dated link ledger](../../public/link-checks/2026-11-07.json): all 46 timestamped baseline URL checks.
- [Baseline feed checks](public-baseline-checks.json): exact source/live comparisons, schema, activities and disabled collection.
- Post-publication checks are recorded separately after the new research snapshot is committed.
