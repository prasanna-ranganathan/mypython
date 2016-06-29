#!/usr/bin/env python

import socket
tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
tcpsocket.bind(("0.0.0.0",8000))
tcpsocket.listen(2)
print "Waiting foa client..."
(client, ( ip,port)) = tcpsocket.accept()

print "Recieved from client: ",ip
client.send("Fuck You")

print

print "Starting ECHO output..."
data = client.recv(2048)

while len(data):
    data = client.recv(2048)
    print "Client data: ",data
    client.send(data)

print "Closing connection..."
client.close()

