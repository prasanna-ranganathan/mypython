#!/usr/bin/python

from __future__ import print_function

with open('/proc/cpuinfo') as file:
    for line in file:
        if line.strip():
            if line.strip('\n').startswith('flags') or line.strip('\n').startswith('Features'):
                if 'lm' in line.strip('\n').split():
                    print("64 Bit")
                else:
                    print("32 Bit")

	
