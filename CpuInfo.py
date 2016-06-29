#!/usr/bin/python

from __future__ import print_function
from collections import OrderedDict
import pprint

def cpuinfo():
	'''Return the information in /proc/cpuinfo
    as a dictionary in the following format:
    cpu_info['proc0']={...}
    cpu_info['proc1']={...}
	'''

	cpuinfo = OrderedDict()
	procinfo = OrderedDict()
	nprocs = 0
	
	with open('/proc/cpuinfo') as file:
	     for line in file:			
		if not line.strip():
	           cpuinfo['proc%s' % nprocs] = procinfo
                   nprocs += 1
            
                   procinfo = OrderedDict()
                else:
                    if len(line.split(':')) == 2:
                        procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                    else:
                        procinfo[line.split(':')[0].strip()] = ''
        return cpuinfo

if __name__ == '__main__':

    cpuinfo = cpuinfo()
    for processor in cpuinfo.keys():
        print(cpuinfo[processor]['model name'])
		
		
