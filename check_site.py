from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parent/'dist'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.refs=[];self.ids=set();self.h1=0;self.titles=0;self.schema=False;self.scripts=[];self.record=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.titles+=1
  for k in ('href','src'):
   if k in a:self.refs.append(a[k])
  if tag=='script' and a.get('type')=='application/ld+json':self.record=True;self.schema=True
 def handle_endtag(self,tag):
  if tag=='script':self.record=False
 def handle_data(self,data):
  if self.record:json.loads(data)
pages={f.name:Page(f.read_text()) for f in ROOT.glob('*.html')}
for name,page in pages.items():
 assert page.h1==1 and page.titles==1,name
 for ref in page.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=unquote(u.path) or name
  assert (ROOT/target).is_file(),(name,ref)
  if u.fragment and target in pages:assert u.fragment in pages[target].ids,(name,ref)
assert (ROOT/'.nojekyll').exists()
print('PASS:',len(pages),'HTML pages, local links/assets, fragment targets, single H1/title and JSON-LD syntax')
