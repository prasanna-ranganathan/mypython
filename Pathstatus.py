#!/usr/bin/env python

import os
def path(pathname):
    print "normcase",os.path.normcase(pathname)
    print "realpath",os.path.realpath(pathname)
    print "abspath",os.path.abspath(pathname)
    print "dirpath",os.path.dirname(pathname)



if __name__ == '__main__':
    path(raw_input())


