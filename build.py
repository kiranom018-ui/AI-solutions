from pathlib import Path
import os,shutil,json,re
from urllib.parse import urlparse
root=Path(__file__).resolve().parent;src=root/'site';out=root/'dist'
if out.exists():shutil.rmtree(out)
shutil.copytree(src,out)
origin=os.environ.get('SITE_URL','').strip().rstrip('/')
if origin and (urlparse(origin).scheme!='https' or not urlparse(origin).netloc or urlparse(origin).query or urlparse(origin).fragment):raise ValueError('SITE_URL must be a verified HTTPS origin or site base URL')
urls=[]
for f in out.glob('*.html'):
 s=f.read_text();title=re.search(r'<title>(.*?)</title>',s).group(1)
 if origin and f.name!='404.html':
  url=origin+('/' if f.name=='index.html' else '/'+f.stem);urls.append(url)
  meta='<link rel="canonical" href="'+url+'"><meta property="og:type" content="website"><meta property="og:site_name" content="James AI Solutions"><meta property="og:title" content="'+title+'"><meta property="og:url" content="'+url+'"><meta name="twitter:card" content="summary">'
  if f.name=='index.html':meta+='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'Organization','name':'James AI Solutions','url':origin+'/'},separators=(',',':'))+'</script>'
 else:meta='<meta name="robots" content="noindex,follow">'
 s=s.replace('</head>',meta+'</head>');f.write_text(s)
(out/'robots.txt').write_text('User-agent: *\n'+('Allow: /\nSitemap: '+origin+'/sitemap.xml\n' if origin else 'Disallow: /\n'))
if origin:(out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>')
print('Built',len(list(out.iterdir())),'files; SEO origin:',origin or 'unset — review build is noindex')
