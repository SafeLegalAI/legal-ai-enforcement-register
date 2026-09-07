import json, subprocess, time
from pathlib import Path
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
rows=[json.loads(l) for l in open('work/agents/actions-a.jsonl',encoding='utf-8')]
urls=sorted({r['source_url'] for r in rows})
archive={}
headers_dir=Path('work/sources/archive-headers'); headers_dir.mkdir(parents=True, exist_ok=True)
for i,u in enumerate(urls,1):
    save='https://web.archive.org/save/'+u
    print(f'archive {i}/{len(urls)} {u}', flush=True)
    res=subprocess.run(['curl','-sI','--max-time','30','-A',UA,save], text=True, capture_output=True)
    hdr=res.stdout + res.stderr
    (headers_dir/(f'{i:02d}.headers')).write_text('URL: '+u+'\nSAVE: '+save+'\nEXIT: '+str(res.returncode)+'\n\n'+hdr, encoding='utf-8')
    loc=None
    for line in hdr.splitlines():
        if ':' in line:
            k,v=line.split(':',1)
            if k.lower() in ('location','content-location'):
                val=v.strip()
                if val:
                    loc=val
    if loc:
        if loc.startswith('//'):
            loc='https:'+loc
        elif loc.startswith('/'):
            loc='https://web.archive.org'+loc
        elif loc.startswith('http://web.archive.org'):
            loc='https://web.archive.org'+loc[len('http://web.archive.org'):]
        archive[u]=loc
    else:
        archive[u]=None
    time.sleep(1)
Path('work/sources/archive-map.json').write_text(json.dumps(archive, indent=2, ensure_ascii=False), encoding='utf-8')
for r in rows:
    loc=archive.get(r['source_url'])
    if loc:
        r['archive_url']=loc
    elif 'archive_url' not in r:
        r['archive_url']=None
with open('work/agents/actions-a.jsonl','w',encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False, separators=(',',':'))+'\n')
print('updated rows', len(rows), 'unique urls', len(urls), 'archives found', sum(1 for v in archive.values() if v))
