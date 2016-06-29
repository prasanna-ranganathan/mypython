#!/usr/bin/env python

from Apache_Log_Parser import gen_find,gen_open,gen_cat
import re

def gen_regex(loglines):
    logpats = r'(\S+) (\S+) (\S+) \[(.*?)\] '\
              r'"(\S+) (\S+) (\S+)" (\S+)(\S+)'

    logpat = re.compile(logpats)

    groups = (logpat.match(line) for line in loglines)
    tuples = (g.groups() for g in groups if g)
    return tuples


filenames = gen_find("access.log",".")
logfiles = gen_open(filenames)
loglines = gen_cat(logfiles)

log = ()

def tuptodict():
    global log
    colnames = ('host','referrer','user','datetime','method','request','proto','status','bytes')
    log = (dict(zip(colnames,t)) for t in gen_regex(loglines))

def field_map(dictseq,name,func):
    for d in dictseq:
        d[name] = func(d[name])
        yield d

log = field_map(log,"status",int)
log = field_map(log,"bytes",lambda s: int(s) if s != '-' else 0)

for r in log:
    print r
