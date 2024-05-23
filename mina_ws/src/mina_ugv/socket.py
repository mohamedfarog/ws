# #!/usr/bin/python

# from websocket import create_connection
# ws = create_connection("ws://192.168.68.56:9090")
# print("Sending 'Hello, World'...")
# ws.send("Hello, World")
# result =  ws.recv()
# print ("Received '%s'" % result)
# ws.close()

#!/usr/bin/env python3

import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:9090") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()