const FEED_URL='https://raw.githubusercontent.com/dotjade/project-neurofreedom/main/public/research-feed.json';
export default {
  async fetch(request, env) {
    const url=new URL(request.url);
    if(url.hostname==='www.tourette.fyi'||url.protocol==='http:'){url.hostname='tourette.fyi';url.protocol='https:';return Response.redirect(url.toString(),308);}
    if(url.pathname==='/api/public-feed'){
      if(request.method!=='GET'&&request.method!=='HEAD')return new Response('Method not allowed',{status:405,headers:{Allow:'GET, HEAD'}});
      try{
        const upstream=await fetch(FEED_URL,{headers:{Accept:'application/json'},cf:{cacheTtl:120,cacheEverything:true},signal:AbortSignal.timeout(4000)});
        if(!upstream.ok)throw new Error('Repository unavailable');
        const text=await upstream.text();if(text.length>64000)throw new Error('Feed too large');
        const feed=JSON.parse(text);
        if(feed.schemaVersion!==1||!Number.isFinite(Date.parse(feed.updatedAt))||Date.parse(feed.updatedAt)>Date.now()+300000||!Array.isArray(feed.timeline)||feed.timeline.length>24||!Array.isArray(feed.activities)||feed.activities.length>6)throw new Error('Invalid feed');
        return new Response(request.method==='HEAD'?null:text,{headers:{'Content-Type':'application/json; charset=utf-8','Cache-Control':'public, max-age=120, no-transform','X-Content-Type-Options':'nosniff','X-Journal-Source':'repository','Referrer-Policy':'no-referrer'}});
      }catch{
        const localUrl=new URL('/research-feed.json',url);const saved=await env.ASSETS.fetch(new Request(localUrl,{method:request.method}));
        const fallback=new Response(saved.body,saved);fallback.headers.set('X-Journal-Source','saved');fallback.headers.set('Cache-Control','public, max-age=60, no-transform');return fallback;
      }
    }
    return env.ASSETS.fetch(request);
  }
};
