#!/usr/bin/python

import os
import sys

def main():
    hostname = sys.argv[1]
    for i in range(255):
        ipadd = hostname + str(i)
        if os.system("ping -c 1 -t 5 -w2 " + ipadd + " > /dev/null 2>&1") == 0:
            print ipadd,"is Up!"
        else:
            print ipadd,"is Down!"
main()

