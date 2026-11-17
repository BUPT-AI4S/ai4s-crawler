"""Collect publisher metadata and search full bibliographies without auto-reviewing."""
import sys
sys.path.insert(0, '/tmp/dlj-2026-deps')
import concurrent.futures as cf
import hashlib
import html
import json
import pathlib
import re
import time
import urllib.parse
from bs4 import BeautifulSoup
from dinglijun_2026_audit import ROOT, OUT, OWN, save, read, fetch
from ai4s_taxonomy import has_ai_evidence
from paper_record import make_record
from nature_meta import record_from_crossref, parse_article_page
from conference_meta import parse_publisher_abstract

SIGNAL = re.compile(r'\b(?:machine[- ]learning|deep[- ]learning|neural|artificial intelligence|AI[- ](?:driven|assisted|enabled|based|powered)|reinforcement learning|random forests?|support vector|gradient boost\w*|xgboost|lightgbm|catboost|Gaussian process|Bayesian optimi\w*|data[- ]driven|large language|foundation model|transformer|generative model|diffusion model|active learning|graph convolution|convolutional|CNN|LSTM|GNN|SVM|genetic algorithm|evolutionary algorithm|symbolic regression|autonomous laborator|self[- ]driving laborator|surrogate model|computer vision|self-supervised|unsupervised learning|supervised learning|representation learning|clustering algorithm|autoencoder|multi-agent|digital twin|few[- ]shot|zero[- ]shot)\b',re.I)

def key(r):return str(r.get('doi') or r['id']).lower()
def text(r):return '\n'.join(str(r.get(k) or '') for k in ['title','abstract','keywords'])
def signal(r):return bool(SIGNAL.search(text(r))) or has_ai_evidence(r)

def worklist():
    records=[];stats=[]
    for s in OWN:
        code=s['code'];a=read(ROOT/f'metadata/{code}/2026/papers.json');b=read(ROOT/f'metadata/{code}/2026/ai4s.json')
        chosen={key(x):x for x in b}; by={key(x):x for x in a}
        for x in a:
            if signal(x) and key(x) not in chosen:chosen[key(x)]=x
        start=len(records)
        for k,x in chosen.items():
            records.append({'key':f"{code}|{x['id']}",'source_code':code,'original_candidate':any(key(z)==k for z in b),'record':x})
        stats.append({'code':code,'title':s['title'],'papers_scanned':len(a),'original_candidates':len(b),'triage_worklist':len(records)-start})
    save(OUT/'worklist.json',records);save(OUT/'worklist-summary.json',stats)
    print('WORKLIST',len(records),'original',sum(x['original_candidate'] for x in records),'additional',sum(not x['original_candidate'] for x in records),flush=True)
    for s in stats:print(s['code'],s['triage_worklist'],s['original_candidates'])

def ijcai():
    soup=BeautifulSoup((OUT/'official/ijcai.html').read_text(),'lxml')
    result=[]
    existing=read(ROOT/'metadata/ijcai/2026/papers.json');by={key(x):x for x in existing}
    for n in soup.select('.paper_wrapper'):
        a=n.select_one('a.title');doi_a=n.find('a',href=re.compile('https://doi.org/'))
        if not a or not doi_a:continue
        doi=doi_a['href'].split('doi.org/')[-1].lower()
        section=n.find_parent(class_='section');track=section.select_one('h3').get_text(' ',strip=True) if section else None
        sub=n.find_parent(class_='subsection');topic=sub.select_one('.subsection_title').get_text(' ',strip=True) if sub else None
        pdf=n.find('a',href=re.compile(r'\.pdf$'))
        row=make_record(id=doi,doi=doi,venue='ijcai',year=2026,title=a.get_text(' ',strip=True),authors=[v.get_text(' ',strip=True) for v in n.select('.authors a')],
             url=urllib.parse.urljoin('https://www.ijcai.org',a['href']),pdf_url=urllib.parse.urljoin('https://www.ijcai.org',pdf['href']) if pdf else None,
             track=track,article_type='Conference Paper',venue_type='conference',source='ijcai.org',published='2026',booktitle='Proceedings of IJCAI 2026')
        row['official_topic']=topic
        result.append(row)
    ids={key(x) for x in result};missing=[x for x in result if key(x) not in by]
    extra=[x for x in existing if key(x) not in ids]
    excluded={'Early Career Spotlight','Sister Conferences Best Papers','Journal Track','Doctoral Consortium','Demo Track'}
    eligible=[x for x in result if x.get('track') not in excluded]
    save(OUT/'ijcai-catalogue.json',{'official_url':'https://www.ijcai.org/proceedings/2026/','checked_at':'2026-11-17','all_catalogue_count':len(result),'eligible_research_count':len(eligible),'excluded_tracks':sorted(excluded),'records':result,'missing_local':[key(x) for x in missing],'local_not_in_official':[key(x) for x in extra]})
    print('IJCAI',len(existing),len(result),'eligible',len(eligible),'missing',len(missing),'extra',len(extra),flush=True)

def nature_catalogues():
    for s in read(OUT/'baseline.json')['sources']:
        code=s['code'];meta=OUT/'official'/f'{code}.json'
        if not meta.exists():continue
        m=read(meta)
        if 'www.nature.com/' not in str(m.get('url')) or m.get('access')!='accessible':continue
        dest=OUT/'nature-catalogues'/f'{code}.json'
        if dest.exists() and read(dest).get('complete'):continue
        first=BeautifulSoup((OUT/'official'/f'{code}.html').read_text(),'lxml')
        pages=[1]+[int(re.search(r'[?&]page=(\d+)',a['href'])[1]) for a in first.select('.c-pagination a[href]') if re.search(r'[?&]page=(\d+)',a['href'])]
        base=m['url'];next_link=first.select_one('.c-pagination a[href*="page="]')
        page_template=urllib.parse.urljoin('https://www.nature.com',next_link['href']) if next_link else base
        result={'source_code':code,'url':base,'year':2026,'checked_at':'2026-11-17','complete':False,'records':[],'pages':max(pages)}
        total=re.search(r'2026\s*\((\d+)\)',first.get_text(' ',strip=True));result['displayed_total']=int(total[1]) if total else None
        seen=set()
        def page(p):
            if p==1:return first
            url=re.sub(r'([?&]page=)\d+',r'\g<1>'+str(p),page_template)
            raw,_,_,_=fetch(url,35)
            return BeautifulSoup(raw,'lxml')
        try:
            with cf.ThreadPoolExecutor(max_workers=3) as ex:
                for p,soup in zip(range(1,max(pages)+1),ex.map(page,range(1,max(pages)+1))):
                    for item in soup.select('article'):
                        a=item.select_one('a[href*="/articles/"]')
                        if not a:continue
                        url=urllib.parse.urljoin('https://www.nature.com',a['href'])
                        if url in seen:continue
                        seen.add(url)
                        result['records'].append({'url':url,'title':a.get_text(' ',strip=True),'listing_text':item.get_text(' ',strip=True),'doi':'10.1038/'+url.split('/articles/')[-1]})
                    save(dest,result)
                    print('NATURE PAGE',code,p,len(result['records']),flush=True)
            result['complete']=result['displayed_total']==len(result['records'])
        except Exception as e:result['error']=str(e)
        old={key(x) for x in read(ROOT/s['papers_path'])};new={x['doi'].lower() for x in result['records']}
        result['missing_local']=sorted(new-old);result['local_not_in_catalogue']=sorted(old-new) if result['complete'] else None
        save(dest,result)
        print('NATURE',code,len(old),len(new),result['displayed_total'],result['complete'],flush=True)

def publisher_one(w):
    r=w['record'];doi=key(r);dest=OUT/'publisher-records'/(hashlib.sha256((r['venue']+'|'+r['id']).encode()).hexdigest()[:24]+'.json')
    if dest.exists():return read(dest)
    url=r.get('publisher_url') or r.get('url') or 'https://doi.org/'+doi
    if 'linkinghub.elsevier.com/retrieve/pii/' in url:url='https://www.sciencedirect.com/science/article/pii/'+url.rsplit('/',1)[-1]
    if r['venue']=='ijcai':url='https://www.ijcai.org/proceedings/2026/'+doi.rsplit('/',1)[-1]
    result={'key':w['key'],'doi':doi,'input_url':url,'checked_at':'2026-11-17','success':False}
    try:
        raw,final,headers,status=fetch(url,22)
        content_type=next((v for k,v in headers.items() if k.lower()=='content-type'),'')
        if 'html' not in content_type.lower():raise ValueError('non-HTML response; not parsed as paper metadata')
        markup=raw.decode('utf8','replace');soup=BeautifulSoup(markup,'lxml')
        if any(t in soup.get_text(' ',strip=True)[:1000].lower() for t in ['verify you are human','just a moment','access denied']):raise ValueError('publisher challenge page')
        def metas(*names):return [x.get('content','').strip() for x in soup.find_all('meta') if (x.get('name') or x.get('property') or '').lower() in {n.lower() for n in names} and x.get('content')]
        gotdoi=metas('citation_doi','dc.identifier','dc.identifier.doi','prism.doi')
        # Require matching DOI when the page exposes one. Otherwise a stable
        # official paper URL and a matching title are checked during review.
        if gotdoi and not any(doi in x.lower() for x in gotdoi):raise ValueError('publisher DOI differs from requested record')
        details=parse_article_page(markup)
        if not details.get('abstract'):details['abstract']=parse_publisher_abstract(markup)
        if not details.get('abstract'):
            node=soup.select_one('#abstracts .abstract.author, #abstracts .abstract, .abstract.author, .abstract-content')
            if node:details['abstract']=re.sub(r'^Abstract\s*','',node.get_text(' ',strip=True),flags=re.I)
        kws=metas('citation_keywords','keywords','dc.subject')
        for node in soup.select('.keywords-section .keyword, .keyword, .Keywords .Keyword, .c-article-subject-list__subject'):
            value=node.get_text(' ',strip=True)
            if value:kws.append(value)
        kws=[html.unescape(x).strip() for v in kws for x in re.split(r';\s*',v) if x.strip()]
        if kws:details['keywords']=list(dict.fromkeys(kws))
        for field,names in [('title',('citation_title','dc.title','og:title')),('authors',('citation_author',)),('pdf_url',('citation_pdf_url',))]:
            values=metas(*names)
            if values:details[field]=values if field=='authors' else values[0]
        result.update(success=True,url=final,status=status,doi_exposed=gotdoi,metadata=details,page_title=soup.title.get_text() if soup.title else None)
        if r['venue']=='ijcai':
            result['metadata']['article_type']='Conference Paper'
            result['metadata']['pdf_url']='https://www.ijcai.org/proceedings/2026/'+doi.rsplit('/',1)[-1].zfill(4)+'.pdf'
        links=[]
        for a in soup.find_all('a',href=True):
            href=a['href']
            if any(host in href for host in ['github.com/','gitlab.com/','zenodo.org/','figshare.com/','huggingface.co/','osf.io/','dataverse']):links.append({'url':href,'text':a.get_text(' ',strip=True)})
        result['research_links']=links
    except Exception as e:result['error']=str(e)
    save(dest,result)
    print('PUBLISHER',w['source_code'],doi,result['success'],len((result.get('metadata') or {}).get('abstract') or ''),len((result.get('metadata') or {}).get('keywords') or []),result.get('error',''),flush=True)
    return result

def publishers():
    records=read(OUT/'worklist.json')
    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        for _ in ex.map(publisher_one,records):pass

if __name__=='__main__':
    {'worklist':worklist,'ijcai':ijcai,'nature':nature_catalogues,'publishers':publishers}[sys.argv[1]]()
