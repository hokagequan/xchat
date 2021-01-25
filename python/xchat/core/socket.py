import asyncio
import websockets

async def hello_server(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

def start_server():
    loop = asyncio.new_event_loop()
    s_server = websockets.serve(hello_server, "localhost", 8765, loop=loop)
    loop.run_until_complete(s_server)
    loop.run_forever()

async def hello_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("Whats your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

def start_client():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(hello_client())
