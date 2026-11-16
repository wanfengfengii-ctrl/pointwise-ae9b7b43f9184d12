"""Retained real raw-source regression/demo; target capability is absent."""
import json,sys
from pathlib import Path
from wire import read
def normal():
 sample=json.loads(Path("sample.json").read_text())
 events=[e for batch in sample["batches"] for e in batch]
 wire="\n".join(json.dumps(e,ensure_ascii=False) for e in events).encode()
 assert list(read([wire[i:i+1] for i in range(len(wire))]))==events
 unicode={"id":["u",1],"kind":"insert","after":None,"char":"水"}
 raw=json.dumps(unicode,ensure_ascii=False).encode()
 assert list(read([raw[:1],raw[1:-1],raw[-1:]]))==[unicode]
 assert list(read([b" \n",b"{}\n"]))==[{}]
 try:list(read([b"{invalid}\n"]))
 except json.JSONDecodeError:pass
 else:raise AssertionError("Invalid source accepted")
 assert sample["expected_text"][1]=="cat" and len(events)==7
 return events
if __name__=="__main__":
 events=normal()
 if sys.argv[1:]==["demo"]:
  print(json.dumps({"scope":"raw source events only; target merge/index not implemented","events":events},ensure_ascii=False))
 else:print("RAW_SOURCE_REGRESSION_OK: byte-fragment decoding, Unicode, raw events and rejection checked; target not implemented")
