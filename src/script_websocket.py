import asyncio
from datetime import datetime

import websockets


async def hello():
    async with websockets.connect("ws://192.168.1.4:8765") as websocket:
        for i in range(1000):
            await websocket.send(f"{datetime.now()} vai tomar no cú 3 {i}")
            r = await websocket.recv()
            print(r)

asyncio.run(hello())
