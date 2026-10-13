import {mkdir,copyFile,cp,readFile} from 'node:fs/promises';
const root=new URL('../',import.meta.url);
await mkdir(new URL('dist/server/',root),{recursive:true});await mkdir(new URL('dist/.openai/',root),{recursive:true});
await copyFile(new URL('worker/index.js',root),new URL('dist/server/index.js',root));
await copyFile(new URL('.openai/hosting.json',root),new URL('dist/.openai/hosting.json',root));
await cp(new URL('drizzle/',root),new URL('dist/.openai/drizzle/',root),{recursive:true});
const source=await readFile(new URL('dist/server/index.js',root),'utf8');const mod=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));if(typeof mod.default.fetch!=='function'||typeof mod.default.scheduled!=='function')throw new Error('Invalid ESM artifact');
console.log('Built dependency-free Worker ESM artifact with D1 migration metadata. Site identity and deployment are still pending.');
