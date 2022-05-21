import asyncio
import threading
from functools import partial

def _run_aio_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
    
    
def starting_process():      
    aioloop = asyncio.new_event_loop()
    t = threading.Thread(target=partial(_run_aio_loop, aioloop), name="Thread_1")
    t.daemon = True  # Необязательно, в зависимости от того, как планируется закрыть приложение
    t.start() 
    return aioloop   
   