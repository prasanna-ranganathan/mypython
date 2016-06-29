#!/usr/bin/env python

import os,sys
import time

def main():
    f = open("/tmp/daemon-log","w")
    while 1:
        f.write('%s\n' % time.ctime(time.time()))
        f.flush()
        time.sleep(10)


if __name__ == '__main__':
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0);
    except OSError, e:
        print >> sys.stderr, "FOrk #1 failed: %d (%s)" % (e.errno,e.strerror)
        sys.exit(1)

    os.chdir("/")
    os.setsid()
    os.umask(0)

    try:
       pid = os.fork()
       if pid > 0:
           print "Daemon PID %d" % pid
           sys.exit(0)
    except OSError,e:
       print>>sys.stderr, "Fork #2 failed: %d (%s)" % (e.errno,e.strerror)
       sys.exit(1)

main()
