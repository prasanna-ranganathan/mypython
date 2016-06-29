#!/usr/bin/python

import httplib
import sys

def http_request(address,port,resource):
    if not resource.startswith("/"):
        resource = "/" + resource

    try:
        conn = httplib.HTTPConnection(address,port)
        print "HTTP Connection created Successfully"
        req = conn.request('GET',resource)
        print 'Request for %s successfull' % resource

        response = conn.getresponse()
        print 'response status: %s' % response.status
    except sock.error,e:
        print 'HTTP Connection failed: %s' % e
        return False
    finally:
        conn.close()
        print "Connection Closed SuccessFully"
    if response.status in [200,301]:
        return True
    else:
        return False

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-a","--address",dest="address",default='localhost',
                      help="ADDRESS for webserver",metavar="ADDRESS")

    parser.add_option("-p","--port",dest="port",type="int",default=80,
                        help="PORT for webserver",metavar="PORT")

    parser.add_option("-r","--resource",dest="resource",default='index.html',
                        help="RESOURCE to check",metavar="RESOURCE")

    (options,args) = parser.parse_args()
    print 'Options: %s, args: %s' % (options,args)
    check = http_request(options.address,options.port,options.resource)
    print 'http_request returned %s' % check
    sys.exit(not check)

