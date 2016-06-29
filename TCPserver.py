#!/usr/bin/env python

import SocketServer

class EchoHandler(SocketServer


serverAddr = ("0.0.0.0",90000)
server = SocketServer.TCPServer(serverAddr,EchoHandler)
server.serve_forver()
