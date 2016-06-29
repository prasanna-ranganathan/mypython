#!/usr/bin/python

from __future__ import print_function
from collections import OrderedDict

def Meminfo():
	meminfo = OrderedDict()
	
	with open('/proc/meminfo') as file:
		for line in file:
			meminfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
	return meminfo

if __name__ == '__main__':
	meminfo = Meminfo()
	print('Total memory: {0}'.format(meminfo['MemTotal']))
	print('Free memory: {0}'.format(meminfo['MemFree']))

