import re,os,json,urllib.request,urllib.parse,html
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36','Accept':'text/html,image/*,*/*'}
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25); return r.read(), r.headers.get('content-type','')
log={}
for line in open('grab/list.txt'):
    line=line.strip()
    if not line: continue
    slug,url=line.split(None,1); d='grab/out/'+slug; os.makedirs(d,exist_ok=True)
    try:
        b,ct=get(url)
        if ct.startswith('image'):
            ext=ct.split('/')[1].split(';')[0].replace('jpeg','jpg').replace('svg+xml','svg')
            open(d+'/img.'+ext,'wb').write(b); log[slug]='image '+str(len(b)); continue
        h=b.decode('utf-8','ignore'); cands=[]
        for m in re.finditer(r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]*content=["\']([^"\']+)',h,re.I): cands.append(('og',m.group(1)))
        for m in re.finditer(r'<link[^>]+rel=["\'][^"\']*(?:apple-touch-icon|icon)[^"\']*["\'][^>]*href=["\']([^"\']+)',h,re.I): cands.append(('icon',m.group(1)))
        for m in re.finditer(r'<img[^>]*>',h,re.I):
            t=m.group(0)
            if re.search(r'logo',t,re.I):
                s=re.search(r'(?:src|data-src|data-lazy-src)=["\']([^"\']+)',t)
                if s: cands.append(('logo',s.group(1)))
        for m in re.finditer(r'<svg[^>]*(?:class|id|aria-label)=["\'][^"\']*logo[^"\']*["\'][\s\S]*?</svg>',h,re.I):
            open(d+'/inline-%d.svg'%len(os.listdir(d)),'w').write(m.group(0))
        seen=set(); got=[]
        for k,(kind,u) in enumerate(cands[:14]):
            u=urllib.parse.urljoin(url,html.unescape(u))
            if u in seen or u.startswith('data:'): continue
            seen.add(u)
            try:
                bb,c2=get(u); ext=os.path.splitext(urllib.parse.urlparse(u).path)[1][:5] or '.bin'
                open('%s/%02d-%s%s'%(d,k,kind,ext),'wb').write(bb); got.append(u)
            except Exception as e: got.append('fail '+u+' '+str(e)[:60])
        log[slug]={'title':(re.search(r'<title[^>]*>([^<]*)',h) or [None,''])[1][:80],'got':got}
    except Exception as e: log[slug]='ERR '+str(e)[:120]
json.dump(log,open('grab/out/log.json','w'),indent=1)
