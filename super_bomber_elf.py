import asyncio
import json
import getch
# import future
from websockets import connect


def play(arg):
  validCommands = [{"l" : {"command":"Look"}}, {"r" : {"command":"DropBomb"}},  {"na" : {"command":["SetName","<name>"]}}
  ,"n" : {"command":"MoveNorth"}, "s" :{"command":"MoveSouth"}, "e" : {"command":"MoveEast"}, "a" : {"command":"MoveWest"}] 
  return validCommands[arg]

async def hello(uri):
    async with connect(uri) as websocket:
        # await websocket.send("Hello world!")
        response = await websocket.recv()
        print(response)
        await websocket.send(json.dumps({"command":["SetName","PowerRangers"]}))
        
        while(True):
          command = getch.getch()

          await websocket.send(json.dumps(play(command)))
          await asyncio.Future()

        # commansd we pass na

        
        # await websocket.send(json.dumps({"command":"MoveEast"}))
        # await websocket.send(json.dumps({"command":"MoveWest"}))
        # await websocket.send(json.dumps({"command":"MoveSouth"}))
        # await websocket.send(json.dumps({"command":"Look"}))

asyncio.run(hello("ws://172.16.173.86:8080/"))