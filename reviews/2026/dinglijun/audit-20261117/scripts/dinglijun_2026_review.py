"""Review ledger: only explicitly assessed records get final decisions."""
import json
import re
import sys
from dinglijun_2026_audit import ROOT, OUT, OWN, save, read

DOMAIN={'life':'AI 用于生命科学','earth':'AI 用于地球宇宙科学','materials':'AI 用于物质科学','math':'AI 用于数理科学','engineering':'AI 用于工程科学','information':'AI 用于信息科学'}
def decisions(entries):
    work=read(OUT/'worklist.json');path=OUT/'semantic-decisions.json';ledger=read(path) if path.exists() else {}
    for i,decision,domain,note,*labels in entries:
        w=work[i];ledger[w['key']]={'decision':decision,'domain':domain,'rationale':note,'labels':labels,'basis':'assistant semantic assessment of title, original abstract and indicated source evidence','worklist_index':i}
    save(path,ledger);print('ASSESSED',len(ledger))

def show(codes,limit=100,start=0):
    from dinglijun_2026_enrich import SIGNAL
    d=read(OUT/'worklist.json');matches=[(i,x) for i,x in enumerate(d) if x['source_code'] in codes]
    for i,w in matches[start:start+limit]:
        r=w['record'];a=r.get('abstract') or ''
        sentences=re.split(r'(?<=[.!?])\s+',a)
        evidence=[s for s in sentences if SIGNAL.search(s)]
        quote=' / '.join(evidence)[:340] or a[:160] or 'MISSING ABSTRACT'
        print(f"{i}|{'C' if w['original_candidate'] else 'N'}|{r['article_type']}|{r['title']}|{quote}")
    print('SOURCE RECORDS',len(matches),'SHOWN',len(matches[start:start+limit]))

if __name__=='__main__':
    if sys.argv[1]=='show':show(sys.argv[2].split(','),int(sys.argv[3]) if len(sys.argv)>3 else 100,int(sys.argv[4]) if len(sys.argv)>4 else 0)
