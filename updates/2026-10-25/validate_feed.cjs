const fs=require('fs');
const allowedActivityIds=['hand-at-ease','familiar-route','notice-one-thing','music-or-silence','small-silly-mark','rest-or-leave'];
let currentFeed=null;
const safeUrl=value=>{try{const u=new URL(value);return u.protocol==='https:'&&!u.username&&!u.password?u.href:null;}catch{return null;}};
function validFeed(feed){if(!feed||feed.schemaVersion!==1||!/^\d{4}-\d{2}-\d{2}T/.test(feed.updatedAt)||!Number.isFinite(Date.parse(feed.updatedAt))||Date.parse(feed.updatedAt)>Date.now()+300000||!/^\d{4}-\d{2}-\d{2}$/.test(feed.lastResearchDate)||feed.lastResearchDate>feed.updatedAt.slice(0,10))return false;
 for(const [key,max] of [['timeline',24],['findings',12],['activities',6]])if(!Array.isArray(feed[key])||feed[key].length>max)return false;
 const text=(v,max=1600)=>typeof v==='string'&&v.length<=max&&!v.includes('\u2014');
 if(!text(feed.latestSummary)||!feed.timeline.every(e=>text(e.title,200)&&text(e.summary)&&text(e.type,100)&&/^\d{4}-\d{2}-\d{2}$/.test(e.date)&&e.date<=feed.lastResearchDate&&safeUrl(e.record)))return false;
 if(!feed.findings.every(e=>text(e.title,200)&&text(e.summary)&&text(e.type,100)&&text(e.label,200)&&text(e.linkState,200)&&/^\d{4}-\d{2}-\d{2}$/.test(e.checkedAt)&&safeUrl(e.url)))return false;
 if(!feed.activities.every(e=>allowedActivityIds.includes(e.id)&&['title','kind','intro','seated','standing','rest'].every(k=>text(e[k]))&&(e.food===undefined||text(e.food))))return false;
 if(feed.activityEditionDate!==undefined&&(!/^\d{4}-\d{2}-\d{2}$/.test(feed.activityEditionDate)||feed.activityEditionDate>feed.updatedAt.slice(0,10)))return false;
 if(feed.featuredActivityId!==undefined&&!feed.activities.some(a=>a.id===feed.featuredActivityId))return false;
 return new Set(feed.activities.map(a=>a.id)).size===feed.activities.length;
}
const feed=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
if(!validFeed(feed)) throw new Error('Invalid feed');
if(feed.feedback.enabled || feed.feedback.sampleSize || feed.feedback.aggregates.length || feed.feedback.trend.length) throw new Error('Feedback must remain disabled and empty');
if(feed.timeline.some((e,i)=>i && e.date>feed.timeline[i-1].date)) throw new Error('Timeline order');
console.log('Feed passes deployed schema, chronological order and disabled-feedback checks.');
