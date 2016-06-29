#!/usr/bin/env python

import commands
import os,sys


def status(path):
    (status,output) = commands.getstatusoutput(sys.argv[1])
    if status:
        print sys.stderr.write("ERROR: ")
        sys.exit(1)
    else:
        print output

status(sys.argv[2])
