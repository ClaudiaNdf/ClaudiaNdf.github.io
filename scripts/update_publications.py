#!/usr/bin/env python3
"""Optional ORCID -> website sync. Requires ORCID_CLIENT_ID and ORCID_CLIENT_SECRET.
Public works only. Safely keeps existing publications if fetch fails.
"""
import json, os, pathlib, re, sys, urllib.parse, urllib.request

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'publications.json'
ORCID='0000-0002-3024-0000'

def request(url, *, data=None, headers=None):
    req=urllib.request.Request(url,data=data,headers={'User-Agent':'ClaudiaNeuendorfAcademicWebsite/1.0 (GitHub Pages)',**(headers or {})})
    with urllib.request.urlopen(req,timeout=30) as res:return json.load(res)

def key(v):
    doi=(v.get('doi') or '').lower().strip().removeprefix('https://doi.org/')
    return 'doi:'+doi if doi else 'title:'+re.sub(r'[^a-z0-9]','',(v.get('title') or '').lower())

def classify(work):
    t=(work.get('publication-type') or '').lower()
    if t in ('preprint','working-paper','working-paper-series','posted-content') or 'preprint' in t:
        return 'Preprint'
    return 'Publication'

def textvalue(x):
    return (x or {}).get('value') if isinstance(x,dict) else None

def parse(groups):
    out=[]
    for group in groups:
        for w in group.get('work-summary',[]):
            title=textvalue((w.get('title') or {}).get('title'))
            if not title:continue
            year=textvalue((w.get('publication-date') or {}).get('year'))
            try:year=int(year)
            except (ValueError,TypeError):continue
            doi=None
            for e in (w.get('external-ids') or {}).get('external-id',[]):
                if (e.get('external-id-type') or '').lower()=='doi':doi=e.get('external-id-value');break
            link=('https://doi.org/'+urllib.parse.quote(doi,safe='/') if doi else textvalue(w.get('url')))
            if not link:continue
            out.append({'title':title,'authors':'','year':year,'type':classify(w),'venue':textvalue(w.get('journal-title')) or '', 'url':link,'source':'ORCID',**({'doi':doi} if doi else {})})
    return out

def main():
    cid=os.getenv('ORCID_CLIENT_ID');secret=os.getenv('ORCID_CLIENT_SECRET')
    if not cid or not secret:
        print('ORCID credentials are missing. Keeping CV-based publication file unchanged.')
        return 0
    token=request('https://orcid.org/oauth/token',data=urllib.parse.urlencode({'client_id':cid,'client_secret':secret,'grant_type':'client_credentials','scope':'/read-public'}).encode(),headers={'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded'})['access_token']
    works=request(f'https://pub.orcid.org/v3.0/{ORCID}/works',headers={'Accept':'application/json','Authorization':'Bearer '+token})
    incoming=parse(works.get('group',[]))
    if not incoming:
        print('No usable ORCID works retrieved; refusing to overwrite file.')
        return 1
    existing=json.loads(DATA.read_text(encoding='utf-8'))
    bykey={key(x):x for x in existing}
    bytitle={re.sub(r'[^a-z0-9]','',(x.get('title') or '').lower()):x for x in existing}
    added=0
    for item in incoming:
        k=key(item)
        t=re.sub(r'[^a-z0-9]','',(item['title'].lower()))
        if k in bykey or t in bytitle:
            continue  # curated CV version wins; avoids weakening author names and classifications
        bykey[k]=item;bytitle[t]=item;added+=1
    result=list(bykey.values())
    result.sort(key=lambda x:(-int(x.get('year',0)), x.get('title','').lower()))
    content=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    if DATA.read_text(encoding='utf-8')!=content:DATA.write_text(content,encoding='utf-8')
    print(f'Added {added} new works from ORCID. Total records: {len(result)}.')
    return 0

if __name__=='__main__':
    try:sys.exit(main())
    except Exception as ex:
        print('Sync failed; existing publication file is preserved:',ex,file=sys.stderr)
        sys.exit(1)
