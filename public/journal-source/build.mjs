import assert from 'node:assert/strict';
import { copyFile, mkdir, readFile, rm } from 'node:fs/promises';

// Publish only reviewed journal assets, never the research repository or the
// separate, disabled feedback service. Use the current repository feed as fallback.
const root = new URL('./', import.meta.url);
const output = new URL('./web-build/', root);
const feedURL = new URL('../research-feed.json', root);
const feed = JSON.parse(await readFile(feedURL, 'utf8'));
assert.equal(feed.schemaVersion, 1);
assert.ok(Number.isFinite(Date.parse(feed.updatedAt)), 'Feed must have a valid updatedAt');
assert.ok(Date.parse(feed.updatedAt) <= Date.now() + 300000, 'Feed cannot be future dated');
assert.ok(Array.isArray(feed.timeline) && feed.timeline.length <= 24);
assert.ok(Array.isArray(feed.findings) && feed.findings.length <= 12);
assert.ok(Array.isArray(feed.activities) && feed.activities.length <= 6);
const feedback = JSON.parse(await readFile(new URL('feedback-config.json', root), 'utf8'));
assert.equal(feedback.enabled, false, 'Shared voting remains disabled');
assert.equal(feedback.apiOrigin, null, 'No feedback service is authorized');
await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
for (const name of ['index.html', 'journal.css', 'journal.js', 'feedback-config.json', 'tourette-qr.svg', '_headers']) {
  await copyFile(new URL(name, root), new URL(name, output));
}
await copyFile(feedURL, new URL('research-feed.json', output));
console.log('Built seven public journal assets; feedback service excluded.');
