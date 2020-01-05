#!/usr/bin/env python

# WS server example

import asyncio
import websockets

room_sockets = set()
room_sockets_to_remove = set()


async def send_to_room(room_socket, message):
    try:
        await room_socket.send(message)
    except websockets.exceptions.ConnectionClosed:
        room_sockets_to_remove.add(room_socket)


async def send_to_rooms(message):
    for room_socket in room_sockets_to_remove:
        room_sockets.discard(room_socket)

    for room_socket in room_sockets:
        await send_to_room(room_socket, message)


async def handler(websocket, path):
    name = await websocket.recv()
    print(f"Handling {name}")

    if name == 'ROOM':
        room_sockets.add(websocket)

    async for message in websocket:
        await send_to_rooms(message)


print("Starting the server on port 8765")
start_server = websockets.serve(handler, port=8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
