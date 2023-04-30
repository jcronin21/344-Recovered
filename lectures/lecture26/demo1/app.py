# To test on the command line: 
#   Mac:        python3 -m websockets ws://localhost:8081/
#   Mac:        python -m websockets ws://localhost:8081/
#   Windows:    py -m websockets ws://localhost:8081/

import asyncio
import websockets

 # IRL, this should be set via an environment variable:
PORT = 8081    

async def echo(websocket):
    print('A client just connected.')
    
    # asynchronous loop
    async for message in websocket:
        print('received message from client:', message)
        await websocket.send('Pong: ' + message)


async def main():
    async with websockets.serve(echo, "", PORT):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    print('Starting web socket server...')
    asyncio.run(main())