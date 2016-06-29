#!/usr/bin/env python
import os,sys
import argparse

def interfaces():
   for i in os.listdir('/sys/class/net/'):
       print i,

def Main():
   parser = argparse.ArgumentParser(description="Interface Check")
   parser.add_argument("-l","--list", help="list available interfaces",action='store_true',default=False)
   parser.add_argument("-i","--iface", type=str, help="interface to check")
   args = parser.parse_args()


   if args.list:
        interfaces()

   if args.iface:
        with open("/sys/class/net/" + args.iface + "/carrier","r") as f:
            if f.read().strip() == "1":
                print args.iface + " is Up"
                raise SystemExit,sys.exit(0)

            else:
                print args.iface + " is Down"
                raise SystemExit,sys.exit(2)

if __name__ == '__main__':
   try:
        Main()
   except IOError:
       print "No such Interface"
