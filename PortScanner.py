#!/usr/bin/python
import socket
ip = raw_input("Enter Ip address")
port = input("Enter Pot address")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if sock.connect_ex((ip,port)):
  print "Port",port, "is Closed"
else:
  print "Port",port,"is Open"
