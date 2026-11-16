"""Original NDJSON source reader, not the requested merge/index implementation."""
import codecs,json
def read(chunks):
 decoder=codecs.getincrementaldecoder("utf-8")();pending=""
 for chunk in chunks:
  pending+=decoder.decode(chunk)
  while "\n" in pending:
   line,pending=pending.split("\n",1)
   if line.strip():yield json.loads(line)
 pending+=decoder.decode(b"",final=True)
 if pending.strip():yield json.loads(pending)
