import re, json, os, html, time, urllib.parse, urllib.request
from playwright.sync_api import sync_playwright
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
out={}
os.makedirs('cand',exist_ok=True); os.makedirs('scrape/out',exist_ok=True)
def plain(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=20).read().decode('utf-8','ignore')
# sitemaps
sm={}
for site in ['https://oakdermatology.com','https://www.defineclinic.com','https://www.belleviemedical.com','https://modernaestheticsmd.com','https://injectionartistryclinic.com','https://www.revance.com','https://dorisdaymd.com','https://drbusso.com','https://www.scarlessnose.com']:
    urls=[]
    for p in ['/sitemap.xml','/sitemap_index.xml','/page-sitemap.xml','/wp-sitemap.xml']:
        try:
            x=plain(site+p); found=re.findall(r'<loc>([^<]+)</loc>',x)
            for f in found[:60]:
                if f.endswith('.xml'):
                    try: urls+=re.findall(r'<loc>([^<]+)</loc>',plain(f))
                    except: pass
                else: urls.append(f)
        except Exception as e: pass
    sm[site]=sorted(set(urls))
json.dump(sm,open('scrape/out/sitemaps.json','w'),indent=1)
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(user_agent=UA,locale='en-US'); pg=ctx.new_page()
    for line in open('scrape/queries.txt'):
        line=line.strip()
        if not line or line.startswith('#'): continue
        kind,slug,q=line.split('|',2)
        res=[]
        try:
            if kind=='img':
                pg.goto('https://www.bing.com/images/search?q='+urllib.parse.quote(q)+'&form=HDRSC2',timeout=40000); pg.wait_for_timeout(2500)
                for m in pg.eval_on_selector_all('a.iusc','els=>els.map(e=>e.getAttribute("m"))')[:12]:
                    try: j=json.loads(m); res.append({'murl':j.get('murl'),'turl':j.get('turl'),'purl':j.get('purl'),'t':j.get('t')})
                    except: pass
            elif kind=='brave':
                pg.goto('https://search.brave.com/images?q='+urllib.parse.quote(q),timeout=40000); pg.wait_for_timeout(4000)
                items=pg.eval_on_selector_all('img','els=>els.map(e=>[e.currentSrc||e.src,e.alt,e.naturalWidth,(e.closest("a")||{}).href||""])')
                res=[{'murl':u,'t':a,'w':w,'purl':h} for u,a,w,h in items if u and w and w>60 and 'brave' not in u.split('/')[2]][:14]
                if not res: res=[{'murl':u,'t':a,'w':w,'purl':h} for u,a,w,h in items if u and w and w>60][:14]
            elif kind=='braveweb':
                pg.goto('https://search.brave.com/search?q='+urllib.parse.quote(q),timeout=40000); pg.wait_for_timeout(3000)
                res=pg.eval_on_selector_all('a[href^="http"]','els=>els.map(e=>({url:e.href,t:e.innerText.slice(0,120)}))')
                res=[r for r in res if 'brave.com' not in r['url']][:25]
            elif kind=='page':
                pg.goto(q,timeout=40000); pg.wait_for_timeout(3000)
                imgs=pg.eval_on_selector_all('img','els=>els.map(e=>[e.currentSrc||e.src||e.dataset.src,e.alt,e.naturalWidth])')
                og=pg.eval_on_selector_all('meta[property="og:image"]','els=>els.map(e=>e.content)')
                res=[{'murl':u,'t':a,'w':w} for u,a,w in imgs if u and w and w>80]+[{'murl':u,'t':'og'} for u in og]
                res=res[:40]
        except Exception as e: res=[{'err':str(e)[:150]}]
        os.makedirs(f'cand/{slug}',exist_ok=True)
        for i,r in enumerate(res if kind not in ('braveweb',) else []):
            for key in ('murl','turl'):
                if not r.get(key): continue
                try:
                    resp=ctx.request.get(r[key],timeout=15000)
                    d=resp.body()
                    if resp.ok and len(d)>1500:
                        ext='svg' if d[:300].lstrip().startswith((b'<?xml',b'<svg')) else 'img'
                        open(f'cand/{slug}/{i}.{ext}','wb').write(d); r['file']=f'cand/{slug}/{i}.{ext}'; break
                except Exception as e: r['err']=str(e)[:60]
        out[slug+'|'+q]=res
    b.close()
json.dump(out,open('scrape/out/bing.json','w'),indent=1)
