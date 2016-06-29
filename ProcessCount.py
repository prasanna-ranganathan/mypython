#!/usr/bin/python

from __future__ import print_function
import os

def Process_list():
	pids = []
	
	for subdir in os.listdir('/proc'):
		if subdir.isdigit():
			pids.append(subdir)
	return pids


if __name__ == '__main__':
	processlist = Process_list()
	print("No of Process:: {0}".format(len(processlist)))
