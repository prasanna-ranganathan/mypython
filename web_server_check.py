#!/usr/bin/python

import re
import socket
import sys

def check_server(address,port,resource):
    if not resource.startswith("/"):
        resource = "/" + resource
    request_string = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (resource,address)
    print 'HTTP request:'
    print '|||%s|||' % request_string

    #create Socket
    s = socket.socket()
    print "Attempting to connect to %s and port %s" % (address,port)
    try:
        s.connect((address,port))
        print "Connected to %s to %s" % (address,port)
        s.send(request_string)
        rsp = s.recv(100)
        print 'Recieved 100 bytes of HTTp Response'
        print '|||%s|||' % rsp
    except socket.error, e:
        print "Connection to %s to port %s failed: %s" % (address,port,e)
        return False
    finally:
        print "Closing the connection"
        s.close()
    lines = rsp.splitlines()
    print "First line of HTTP Response: %s " % lines[0]
    try:
        version,status,message = re.split(r'\s+',lines[0],2)
        print "Version: %s, status: %s, message: %s" % (version,status,message)
    except ValueError:
        print 'Failed to split status line'
        return False
    if status in ['200','301']:
        print 'Success: status was -' % status
        return True
    else:
        print "Failure: status %s " % status
        return False

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-a","--address",dest="address",default="localhost",
                      help="ADDRESS for webserver",metavar="ADDRESS")

    parser.add_option("-p","--port",dest="port",type="int",default=80,
                      help="Port for webserver",metavar="PORT")

    parser.add_option("-r","--resource",dest="resource",default="index.html",
                      help="resourse for webserver",metavar="resource")

    (options, args) = parser.parse_args()
    print 'options: %s, args: %s' % (options, args)
    check = check_server(options.address, options.port, options.resource)
    print 'check_webserver returned %s' % check
    sys.exit(not check)


