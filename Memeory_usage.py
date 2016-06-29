#!/usr/bin/env python

import resource,sys

"""
def memory_usage():
    process = ps.util.Process(os.getpid())
    mem = process.get_memeory_info()[0] /float(2 ** 20)
    return mem

print memory_usage()
"""


def memory_usage():
    rusage_denom = 1024
    if sys.platform == 'linux2':
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss /rusage_denom
    return mem

print memory_usage()
