# Public feed, optional activities and bounded link check

Checked 6 November 2026, 02:51-02:54 UTC. Read-only review of the prepublication edition.

## Verified baseline

- Remote main read through the GitHub connector: `cd78cc307253a3c38ee3b846849150721ea19264`.
- README, RESEARCH_PROTOCOL, STATUS and public/journal-source/README fetched at that exact head match the latest local November 5 snapshot. The current plan advances the H13 McGuire 2020 audit; closed mask/provenance work must not be repeated absent new inputs.
- Connector feed blob: `ec7e6528af7891fa152b2529b5772ddb30234d5d`.
- Production API and anonymous raw GitHub both returned HTTP 200 and exactly match connector bytes. Feed SHA-256: `1f5afc0f5636a75c50cb17bca80530b3abcdb3842d6c818f90c1a3e78dfbb768`.
- Production reports `X-Journal-Source: repository`. The edition is November 5, `updatedAt=2026-11-05T02:45:19Z`, `lastResearchDate=2026-11-05`, `activityEditionDate=2026-11-05`, `featuredActivityId=rest-or-leave`.
- Schema version 1; 24 descending timeline entries, 3 findings, 6 unique approved activities. All timeline dates precede or equal the research date. No visible em dash in feed data.
- The homepage returned HTTP 200, its bytes exactly match the known source, the introduction anchor exists, and there is no HTML form. This is source/HTTP inspection, not rendered UI or accessibility verification.

## Activity and collection review

All six activities exactly match the saved source catalog: hand-at-ease, familiar-route, notice-one-thing, music-or-silence, small-silly-mark, rest-or-leave. Each has seated, standing and rest alternatives. Usual supports, comfort, imagining and skipping remain available. There are no exertion targets, breath holds, suppression tasks, timers, streaks or food activities. The live page says these are ordinary leisure ideas, not proven tic or ADHD treatments; users need not hold back tics and should stop if uncomfortable. It labels the selection as a fixed-catalog choice rather than new research or a clinical recommendation.

The feed has feedback disabled, zero sample size, and empty aggregates/trend. Live feedback-config.json returned HTTP 200 with enabled=false, apiOrigin=null and verifiedAt=null. The live page says reflection is neither sent nor saved. Source JavaScript reviewed against the snapshot uses page-memory reflection and has no localStorage/sessionStorage/sendBeacon. This is not a fresh end-to-end network/rendering audit.

## Bounded links: 46 URLs, 02:52:54-02:53:34 UTC

The pass checked all 24 current timeline links, 3 finding links, 6 static fallback research records, 9 homepage source links, homepage, production API, raw feed and feedback config. Requests were ordinary anonymous curl GETs with redirects, no credentials, custom agent, security override or bypass.

- 30 GitHub research records: HTTP 200, expected repository path and rendered-article marker present.
- CDC Tourette introduction, MedlinePlus Genetics and ONLINE-TICS publisher page: HTTP 200 with expected identity text.
- Ivanova 2026 primary PDF: HTTP 200, PDF signature and DOI 10.1186/s44247-026-00284-7 verified in extracted text.
- Isaacs PMC10863457: HTTP 203 challenge/access-limited response, target content not verified in this pass.
- Six PubMed homepage citations (21955933, 16520330, 17987065, 25264251, 25044024, 26041822): HTTP 203 challenge/access-limited responses; target contents not verified in this pass.
- Pappert publisher DOI 10.1212/01.WNL.0000086370.10186.7C: HTTP 403 bot/access challenge; not established broken. A historical claim about a lawful institutional copy was not freshly rechecked.
- Homepage, production API, anonymous raw feed and feedback config: HTTP 200.

Total: 38 retrievable/identity-confirmed endpoints and 8 access-limited endpoints. No 404/410 or confirmed broken link. Canonical source URLs should remain; access limits should not be called source failures.

## Integration notes

1. Findings' displayed checkedAt fields still say November 2. Today's actual checks support November 6 dates and route-specific labels: Isaacs access-limited HTTP 203; Pappert publisher challenge HTTP 403; Ivanova primary PDF retrieved HTTP 200. Do not imply the institutional Pappert copy was verified today.
2. The feed is already at its 24-entry renderer limit. Adding November 6 requires dropping the oldest feed entry only; preserve its permanent research file.
3. The known static fallback still dates its saved edition October 13 and the static next-question remains ONLINE-TICS, behind current STATUS. This is an existing, documented static-source limitation, not a new feed regression. A feed-only change cannot fix it.
4. This baseline predates any November 6 publication. Verify new links and exact source/production bytes after publication; these checks do not establish a future edition.
5. No rendered/mobile/zoom/physical-keyboard/narration test, accessibility certification or clinical activity-safety certification is claimed.

Detailed machine-readable ledger: [dated link checks](../../public/link-checks/2026-11-06.json). This review precedes the November 6 feed update; the separate publication receipt records subsequent verification.
