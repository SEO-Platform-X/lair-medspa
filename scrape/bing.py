import re, json, urllib.request, urllib.parse, os, html, sys
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36','Accept-Language':'en-US,en;q=0.9'}
def get(u,b=False):
    r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20); d=r.read()
    return d if b else d.decode('utf-8','ignore')
out={}
os.makedirs('cand',exist_ok=True)
for line in open('scrape/queries.txt'):
    line=line.strip()
    if not line or line.startswith('#'): continue
    kind,slug,q=line.split('|',2)
    res=[]
    try:
        if kind=='img':
            h=get('https://www.bing.com/images/search?form=HDRSC2&first=1&q='+urllib.parse.quote(q))
            for m in re.finditer(r'm="(\{[^"]+\})"',h):
                try: j=json.loads(html.unescape(m.group(1)))
                except: continue
                if 'murl' in j: res.append({'murl':j['murl'],'purl':j.get('purl'),'t':j.get('t'),'turl':j.get('turl')})
            res=res[:10]
            os.makedirs(f'cand/{slug}',exist_ok=True)
            for i,r in enumerate(res):
                for key in ('murl','turl'):
                    try:
                        d=get(r[key],True)
                        if len(d)>2000:
                            ext='svg' if d[:200].lstrip().startswith((b'<?xml',b'<svg')) else 'img'
                            open(f'cand/{slug}/{i}.{ext}','wb').write(d); r['file']=f'cand/{slug}/{i}.{ext}'; r['via']=key; break
                    except Exception as e: r['err_'+key]=str(e)[:60]
        else:
            h=get('https://www.bing.com/search?q='+urllib.parse.quote(q))
            for m in re.finditer(r'<li class="b_algo".*?<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>.*?(?:<p[^>]*>(.*?)</p>|</li>)',h,re.S):
                res.append({'url':m.group(1),'title':re.sub('<.*?>','',m.group(2)),'snip':re.sub('<.*?>','',m.group(3) or '')[:200]})
            res=res[:8]
    except Exception as e: res=[{'err':str(e)[:100]}]
    out[slug+'|'+q]=res
json.dump(out,open('scrape/out/bing.json','w'),indent=1)
