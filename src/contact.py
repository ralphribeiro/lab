import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://192.168.1.5:8001") as websocket:
        for i in range(1000):
            await websocket.send(f"Hello world! {i}")
            print(await websocket.recv())
            

asyncio.run(hello())