import asyncio
import json
# import future
from websockets import connect

async def hello(uri):
    async with connect(uri) as websocket:
        # await websocket.send("Hello world!")
        response = await websocket.recv()
        print(response)

        # await websocket.send(json.dumps({"command":["SetName","John and Naomi"]}))
        await websocket.send(json.dumps({"command":"MoveNorth"}))
        await asyncio.Future()

asyncio.run(hello("ws://172.16.173.86:8080/"))