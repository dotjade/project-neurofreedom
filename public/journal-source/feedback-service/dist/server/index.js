const ORIGIN='https://tourette.fyi';
const IDS=new Set(['hand-at-ease','familiar-route','notice-one-thing','music-or-silence','small-silly-mark','rest-or-leave']);
const DAY_CAP=2000;
const ACTIVITY_CAP=1000;
export async function purgeExpired(db,now=new Date()){
  const threshold=new Date(Date.UTC(now.getUTCFullYear(),now.getUTCMonth(),now.getUTCDate())-29*86400000).toISOString().slice(0,10);
  return db.batch([db.prepare('DELETE FROM activity_votes WHERE day < ?').bind(threshold),db.prepare('DELETE FROM day_totals WHERE day < ?').bind(threshold)]);
}
function headers(origin){const h={'Content-Type':'application/json; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Referrer-Policy':'no-referrer','Vary':'Origin'};if(origin===ORIGIN)h['Access-Control-Allow-Origin']=ORIGIN;return h;}
function reply(value,status=200,origin){return new Response(JSON.stringify(value),{status,headers:headers(origin)});}
async function smallJson(request){if(!request.headers.get('Content-Type')?.startsWith('application/json'))throw new Error('type');if(Number(request.headers.get('Content-Length')||0)>96)throw new Error('size');const reader=request.body?.getReader();if(!reader)throw new Error('body');const chunks=[];let size=0;while(true){const {value,done}=await reader.read();if(done)break;size+=value.byteLength;if(size>96){await reader.cancel();throw new Error('size');}chunks.push(value);}const buffer=new Uint8Array(size);let offset=0;for(const chunk of chunks){buffer.set(chunk,offset);offset+=chunk.length;}return JSON.parse(new TextDecoder().decode(buffer));}
export default {
  async scheduled(event,env){if(env.DB)await purgeExpired(env.DB,new Date(event.scheduledTime));},
  async fetch(request,env){
    const url=new URL(request.url);const origin=request.headers.get('Origin');
    if(url.pathname==='/api/vote'&&request.method==='OPTIONS'){
      if(origin!==ORIGIN||request.headers.get('Access-Control-Request-Method')!=='POST')return reply({error:'Origin not allowed'},403);
      const requested=(request.headers.get('Access-Control-Request-Headers')||'').toLowerCase().split(',').map(x=>x.trim()).filter(Boolean);
      if(requested.some(x=>!['content-type','x-tourette-vote'].includes(x)))return reply({error:'Headers not allowed'},403);
      return new Response(null,{status:204,headers:{...headers(origin),'Access-Control-Allow-Methods':'POST','Access-Control-Allow-Headers':'Content-Type, X-Tourette-Vote','Access-Control-Max-Age':'600'}});
    }
    if(url.pathname==='/api/cleanup'&&request.method==='GET'){
      if(!env.DB)return reply({error:'Storage unavailable'},503,origin);
      try{await purgeExpired(env.DB);return reply({cleaned:true},200,origin);}catch{return reply({error:'Storage unavailable'},503,origin);}
    }
    if(!['/api/summary','/api/vote'].includes(url.pathname))return reply({error:'Not found'},404,origin);
    if(!env.DB||env.PUBLIC_VOTING_ENABLED!=='true'||env.RETENTION_SCHEDULE_CONFIRMED!=='true')return reply({error:'Voting is not open'},503,origin);
    try{
      if(url.pathname==='/api/summary'){
        if(request.method!=='GET')return reply({error:'Method not allowed'},405,origin);
        await purgeExpired(env.DB);
        const records=await env.DB.prepare('SELECT day, activity_id, votes FROM activity_votes ORDER BY day DESC, activity_id').all();
        const days=[];let totalVotes=0;for(const row of records.results||[]){let day=days.find(d=>d.day===row.day);if(!day){day={day:row.day,activities:[]};days.push(day);}day.activities.push({id:row.activity_id,votes:row.votes});totalVotes+=row.votes;}
        return reply({totalVotes,days,retentionDays:30,unit:'votes',uniquePeopleKnown:false},200,origin);
      }
      if(request.method!=='POST')return reply({error:'Method not allowed'},405,origin);
      if(origin!==ORIGIN||request.headers.get('X-Tourette-Vote')!=='v1')return reply({error:'Origin or request header not allowed'},403);
      let payload;try{payload=await smallJson(request);}catch{return reply({error:'A small JSON activity preference is required'},400,origin);}
      if(!payload||typeof payload!=='object'||Array.isArray(payload)||Object.keys(payload).length!==1||!IDS.has(payload.activityId))return reply({error:'Only an allowlisted activityId is accepted'},400,origin);
      const day=new Date().toISOString().slice(0,10);const activityId=payload.activityId;
      await purgeExpired(env.DB);
      // D1 batch is transactional. The conditional update reserves a capped vote.
      // changes() in the following statement records only a successful reservation.
      const result=await env.DB.batch([
        env.DB.prepare('INSERT INTO day_totals (day,votes) VALUES (?,0) ON CONFLICT(day) DO NOTHING').bind(day),
        env.DB.prepare('UPDATE day_totals SET votes=votes+1 WHERE day=? AND votes<? AND COALESCE((SELECT votes FROM activity_votes WHERE day=? AND activity_id=?),0)<?').bind(day,DAY_CAP,day,activityId,ACTIVITY_CAP),
        env.DB.prepare('INSERT INTO activity_votes (day,activity_id,votes) SELECT ?,?,1 WHERE changes()=1 ON CONFLICT(day,activity_id) DO UPDATE SET votes=activity_votes.votes+1').bind(day,activityId)
      ]);
      if(!result[1]?.meta?.changes)return reply({error:'The global vote limit for today has been reached'},429,origin);
      return reply({recorded:true,day,activityId,unit:'vote'},200,origin);
    }catch{return reply({error:'Voting is unavailable'},503,origin);}
  }
};
