#!/usr/bin/env python

import re

def valid(num):
  ph = re.compile('(^[789]*)$')
  if ph.match(num) != None:
    print "YES"
  else:
    print "NO"



def main():
  t = int(raw_input())
  while t > 0:
    valid(raw_input())
    t = t - 1


main()

