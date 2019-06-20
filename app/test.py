# import asyncio
# import websockets
import requests

key = input("EnterYubico Key:")
headers = {"key": str(key)}
r = requests.post("https://demo.yubico.com/api/v1/simple/otp/validate", headers = headers)
print(r.json())

# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")

#     greeting = f"Hello {name}!"

#     await websocket.send(greeting)
#     print(f"> {greeting}")

# start_server = websockets.serve(hello, 'localhost', 8080)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()