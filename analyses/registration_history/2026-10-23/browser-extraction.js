// Read-only DOM extraction, run through the supported browser's evaluate API
// after navigating each URL and waiting for the Study Design heading.
// No browser internals, result measurements, contacts or hidden state accessed.
const metadataFromRenderedPage = () => ['Study Status', 'Study Design', 'Outcome Measures', 'Document Section'].map(name => {
  const heading = Array.from(document.querySelectorAll('h2,h3,h4')).find(e => e.textContent.trim() === name);
  return { heading: name, text: heading?.parentElement.innerText ?? null };
});
// Use the FIRST Outcome Measures heading: a later identically named heading
// is the results section and must not be collected.
const historyIndexFromRenderedPage = () => Array.from(document.querySelectorAll('table tr'))
  .filter(row => row.querySelector('a[href*="tab=history"]'))
  .map(row => ({ text: row.innerText, url: row.querySelector('a[href*="tab=history"]').href }));
// Audited versions: 1, 7, 8, 13, 23, 24, 25. URLs are saved in the extracts.
