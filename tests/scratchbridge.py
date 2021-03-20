import asyncio
import websockets
import os

headers = {
  'Cookie': f'scratchsessionid={os.getenv("sessionid")}',
  'Origin': 'https://scratch.mit.edu'
}
async def send():
  data = ['{"name": "handshake", "user": "ninjaMAR", "project_id": 438906671}','{"method":"set","user":"ninjaMAR","project_id":"438906671","name":"☁ Test3","value":123456789}']
  async with websockets.connect('wss://clouddata.scratch.mit.edu/',extra_headers=headers) as websocket: 
    for i in data:
      await websocket.send(i)
      #response = await websocket.recv()
      #print(response)

asyncio.get_event_loop().run_until_complete(send())