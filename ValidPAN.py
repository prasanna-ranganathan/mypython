#!/usr/bin/python

import re

def main():
  t = int(raw_input())
  while t != 0:
    t = t - 1
    s = raw_input();
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$',s):
      print "YES"
    else:
      print "NO"


main()
