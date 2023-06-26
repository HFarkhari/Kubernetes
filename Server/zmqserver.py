#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq


print('The server app is running.')

context = zmq.Context()
socket = context.socket(zmq.REP)

# Server
socket.bind("tcp://*:5555") 

counter = 0
while True:
    #  Wait for next request from client
    if counter == 0:
    	print('Server is ready to recieve msg from client:\n')
    	counter += 1
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")


