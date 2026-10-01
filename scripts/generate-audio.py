"""Gera arquivos estáticos pt-BR; o jogo não consulta serviços de voz."""
import asyncio,json,os,pathlib,edge_tts
root=pathlib.Path(__file__).resolve().parents[1]
if os.getenv('NODE_EXTRA_CA_CERTS'): edge_tts.communicate._SSL_CTX.load_verify_locations(cafile=os.environ['NODE_EXTRA_CA_CERTS'])
texts=json.loads((root/'src/narrations.json').read_text())
semaphore=asyncio.Semaphore(4)
async def generate(key,text):
 path=root/'public/audio'/f'{key}.mp3'
 if path.exists() and path.stat().st_size>1000:return
 async with semaphore:
  for attempt in range(3):
   try:
    await asyncio.wait_for(edge_tts.Communicate(text,voice='pt-BR-FranciscaNeural',rate='-8%',proxy=os.getenv('HTTPS_PROXY')).save(str(path)),45)
    print(key,'OK',flush=True);return
   except Exception as e:
    if attempt==2: print(key,'FAILED',type(e).__name__,flush=True);raise
async def main(): await asyncio.gather(*(generate(k,t) for k,t in texts.items()))
asyncio.run(main())
