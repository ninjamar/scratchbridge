import asyncio
import websockets
async def send():
  data = ['{"name": "handshake", "user": "ninjaMAR", "project_id": 438906671}','{"method":"set","user":"ninjaMAR","project_id":"438906671","name":"☁ Test3","value":123456789}']
  async with websockets.connect('wss://clouddata.scratch.mit.edu/') as websocket: 
    for i in data:
      await websocket.send(eval(i))
      response = websocket.recv()
      print(response)

asyncio.get_event_loop().run_until_complete(send())
