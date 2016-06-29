#!/usr/bin/env python

import os,re,sys
import fnmatch
import gzip,bz2


def gen_find(filepat,top):
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)


def gen_open(filenames):
    for name in filenames:
        if name.endswith('.gz'):
            yield gzip.open(name)
        elif name.endswith('.bz2'):
            yield bz2.BZ2File(name)
        else:
            yield open(name)

def gen_cat(sources):
    for s in sources:
        for item in s:
            yield item

def gen_grep(pat,lines):
    patc = re.compile(pat)
    for line in lines:
        if patc.search(line):
            yield line
"""
pat = r"{0}".format(sys.argv[1])
logdir = sys.argv[2]

filenames = gen_find("access.log",logdir)
logfiles = gen_open(filenames)
loglines = gen_cat(logfiles)
patlines = gen_grep(pat,loglines)
bytecoloumn = (line.rsplit(None,1)[1] for line in patlines)
bytes = (int(x) for x in bytecoloumn if x != '-')

print "Total",sum(bytes)

"""
