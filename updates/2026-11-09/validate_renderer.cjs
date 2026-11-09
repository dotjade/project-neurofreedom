const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
const path = require('path');
const root = process.argv[2];
const feed = JSON.parse(fs.readFileSync(path.join(root, 'public/research-feed.json')));
const js = fs.readFileSync(path.join(root, 'public/journal-source/journal.js'), 'utf8');
const validatorSource = js.slice(0, js.indexOf('\nfunction link('));
const context = vm.createContext({ URL, Date, document: {} });
vm.runInContext(validatorSource + '\nglobalThis.checkFeed = validFeed;', context);
const tests = [];
function check(name, fn) { assert.ok(fn(), name); tests.push(name); }
function mutation(fn) { const copy=JSON.parse(JSON.stringify(feed)); fn(copy); return copy; }
check('Final feed accepted by actual renderer validator', () => context.checkFeed(feed));
check('Rejects future timestamp', () => !context.checkFeed(mutation(x => x.updatedAt='2099-01-01T00:00:00Z')));
check('Rejects 25 timeline entries', () => !context.checkFeed(mutation(x => x.timeline.push(x.timeline[0]))));
check('Rejects duplicate activity', () => !context.checkFeed(mutation(x => x.activities[1]=x.activities[0])));
check('Rejects unapproved activity', () => !context.checkFeed(mutation(x => x.activities[0].id='unapproved')));
check('Rejects unsafe source URL', () => !context.checkFeed(mutation(x => x.timeline[0].record='javascript:alert(1)')));
check('Rejects public em dash', () => !context.checkFeed(mutation(x => x.latestSummary+='\u2014')));
check('Rejects unapproved selection', () => !context.checkFeed(mutation(x => x.featuredActivityId='unapproved')));
console.log(JSON.stringify({checks:tests,passed:tests.length,scope:'Actual feed-validation function only; not rendered accessibility or narration testing.'}, null, 2));
