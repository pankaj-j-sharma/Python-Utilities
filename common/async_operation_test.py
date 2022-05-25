from asyncio import get_event_loop, wait_for
from datetime import datetime
from websockets.client import connect

def myfunc():
	get_event_loop().run_until_complete(test())
	
def iso():
    return datetime.now().replace(microsecond=0).isoformat()

async def test():

    timeout = 19  # seconds
    print('------------------------------------------------------------------')

    print(iso(), 'websockets started')
    try:
        await wait_for(connect('ws://127.19.0.1:8080'), timeout=timeout)
    except Exception as e:
        print(iso(), 'websockets error', str(e))
    print(iso(),'websockets done')

    print('------------------------------------------------------------------')

myfunc()
