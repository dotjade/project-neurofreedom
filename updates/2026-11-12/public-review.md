# November 12 public-link and optional-activity review

## Fresh result

This bounded replacement review made 48 fresh anonymous requests between `2026-11-12T08:02:42.465672+00:00` and `2026-11-12T08:03:42.789220+00:00`: 39 retrievable targets, eight access-limited targets, and one missing favicon. No research citation was confirmed broken. Earlier November 12 request logs were unavailable and are not used as evidence here.

The [request ledger](../../public/link-checks/2026-11-12.json) contains individual request timestamps and statuses plus 12 passing static safeguard checks. Each request was an ordinary curl GET with redirects, a 30-second timeout and a maximum of five redirects; five workers ran concurrently. No credentials, custom user agent, challenge solving, security override or access bypass was used. No denied request was retried. Response bodies were temporary and deleted; no full-text paper is retained or published.

Coverage comprises 24 current timeline links, three findings, six static fallback research links, nine other homepage research citations, homepage, production API, anonymous raw feed, feedback configuration, runtime and favicon. Repository navigation and contribution links were outside scope. This is not an exhaustive crawl or scientific revalidation.

## Source access

- Thirty GitHub research records returned HTTP 200 with their expected paths and rendered-markdown markers.
- CDC, MedlinePlus Genetics and the ONLINE-TICS publisher page returned HTTP 200 with matching page titles.
- Isaacs PMC10863457 and six PubMed introduction citations returned HTTP 203 access-limited responses. Target article content was not verified.
- Pappert's publisher DOI returned HTTP 403 with a challenge-page title. It is not established broken.
- Ivanova's primary PDF returned HTTP 200 with a PDF signature and DOI `10.1186/s44247-026-00284-7` verified in temporary extracted text.
- Homepage, API, raw feed, configuration and JavaScript returned HTTP 200. The existing favicon returned an empty HTTP 404; that is an asset issue, not a research-citation failure.

Keep canonical primary links. November 12 finding access wording may be:

- Isaacs: “Direct HTTP 203 access-limited response; article content not verified in this pass”.
- Pappert: “Publisher HTTP 403 challenge; source not established broken in this pass”.
- Ivanova: “Primary PDF retrieved with HTTP 200; DOI identity verified”.

## Prepublication baseline and safeguards

The production API and anonymous raw feed matched the surviving local feed, SHA-256 `31f088ff0fd00f83046045b1d2f946ba525e3b508204a0a47d9f4d2653fce5cd`. Both showed updatedAt `2026-11-11T03:21:51Z`, lastResearchDate and activityEditionDate `2026-11-11`, and featuredActivityId `familiar-route`. The API returned the repository-source header. Live homepage, runtime and feedback configuration matched local source bytes. These checks do not establish publication of a November 12 edition.

All six approved activity objects exactly match the saved catalog: hand-at-ease, familiar-route, notice-one-thing, music-or-silence, small-silly-mark and rest-or-leave. Each retains seated, standing and rest alternatives. Source rendering gives rest and skipping equal standing and says to stop if uncomfortable. No new activity or treatment claim was introduced. These are ordinary optional leisure/movement ideas, not established tic or ADHD treatments, and this preservation check is not clinical safety certification. The planned next selection, `notice-one-thing`, is an editorial rotation only; this review did not edit the feed.

Feed feedback remains disabled, with sampleSize zero and empty aggregates/trend. Live and local configuration retain enabled=false, apiOrigin=null and verifiedAt=null. The source gate returns before vote summary requests or controls. No live vote or write was attempted. The homepage has no form; runtime has no localStorage, sessionStorage, sendBeacon or document.cookie usage. Reflection is excluded from narration and clears on pagehide and restored pageshow.

## Limits and handoff

These are HTTP and static-source checks, not dynamic network/voting tests, rendered accessibility certification, mobile/zoom tests, physical keyboard/touch tests or narration verification. No app source, feed, activity catalog, deployment or external state was changed. Static fallback and next-question assets remain unchanged. After publication, verify the new report link, dated feed bytes and repository-source header separately.
