#!/usr/bin/env python
import os,sys
import platform

def Banner(name):
  print "-" * 60
  print name
  print "-" * 60

def main():
  print 'uname:' ,platform.uname()
  print
  print 'System :',platform.system()
  print 'node   :',platform.node()
  print 'Release:',platform.release()
  print 'version:',platform.version()
  print 'Machine:',platform.machine()
  print 'Processor:',platform.processor()

Banner('OS Summary')
main()

