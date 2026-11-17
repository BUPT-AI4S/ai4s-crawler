import re
from pathlib import Path

def parse_bib(text):
 result=[]
 for chunk in re.split(r'(?m)^@',text)[1:]:
  fields={};start=chunk.find(',')+1;i=start
  while i<len(chunk):
   m=re.search(r'(\w+)\s*=\s*',chunk[i:])
   if not m:break
   key=m.group(1).lower();i+=m.end()
   if chunk[i]=='{':
    i+=1;j=i;depth=1
    while i<len(chunk) and depth:
     if chunk[i]=='{' and (i==0 or chunk[i-1]!='\\'):depth+=1
     elif chunk[i]=='}' and (i==0 or chunk[i-1]!='\\'):depth-=1
     i+=1
    val=chunk[j:i-1]
   elif chunk[i]=='"':
    i+=1;j=i
    while i<len(chunk) and not(chunk[i]=='"' and chunk[i-1]!='\\'):i+=1
    val=chunk[j:i];i+=1
   else:
    j=i
    while i<len(chunk) and chunk[i] not in ',\n':i+=1
    val=chunk[j:i].strip()
   fields[key]=val
  if fields:result.append(fields)
 return result
