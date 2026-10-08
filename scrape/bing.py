import re, json, urllib.request, urllib.parse, os, html, time
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36','Accept-Language':'en-US,en;q=0.9','Referer':'https://duckduckgo.com/'}
def get(u,b=False):
    r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20); d=r.read()
    return d if b else d.decode('utf-8','ignore')
def ddg(q):
    h=get('https://duckduckgo.com/?q='+urllib.parse.quote(q)+'&iax=images&ia=images')
    m=re.search(r'vqd=["\']?([\d-]+)',h)
    if not m: return [{'err':'novqd'}]
    j=json.loads(get(f'https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(q)}&vqd={m.group(1)}&f=,,,&p=1'))
    return [{'murl':r['image'],'turl':r.get('thumbnail'),'purl':r.get('url'),'t':r.get('title')} for r in j.get('results',[])][:12]
out={}
os.makedirs('cand',exist_ok=True)
for line in open('scrape/queries.txt'):
    line=line.strip()
    if not line or line.startswith('#'): continue
    kind,slug,q=line.split('|',2)
    try:
        res=ddg(q)
        os.makedirs(f'cand/{slug}',exist_ok=True)
        for i,r in enumerate(res):
            for key in ('murl','turl'):
                if not r.get(key): continue
                try:
                    d=get(r[key],True)
                    if len(d)>1500:
                        ext='svg' if d[:300].lstrip().startswith((b'<?xml',b'<svg')) else 'img'
                        open(f'cand/{slug}/{i}.{ext}','wb').write(d); r['file']=f'cand/{slug}/{i}.{ext}'; r['via']=key; break
                except Exception as e: r['err_'+key]=str(e)[:60]
    except Exception as e: res=[{'err':str(e)[:150]}]
    out[slug+'|'+q]=res
    time.sleep(2)
json.dump(out,open('scrape/out/bing.json','w'),indent=1)
