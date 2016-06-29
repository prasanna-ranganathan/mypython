#!/usr/bin/python

import os
import fnmatch

def gen_find(filepat,top):
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)


if __name__ == '__main__':
    Pyfiles = gen_find("*.py",".")
    for name in Pyfiles:
        print name
