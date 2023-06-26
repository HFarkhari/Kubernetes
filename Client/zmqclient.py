#
#   Hello World client in Python
#   Connects REQ socket to tcp://myzmqserver-service:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq


print('\n\nZMQ client version, use "myzmqserver-service" as server ip, tcp protocol, and 5555 port')
server_ip = 'myzmqserver-service' # default
#server_ip = 'localhost'          
#server_ip = '0.0.0.0'


context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://"+server_ip+":5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} …")
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
    
    
    
    
    
    
