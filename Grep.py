#!/usr/bin/env python : Patch# 152: (Release 15.1.1.1: PGL 1) failed

import os,sys
import re
os.system('clear')

def banner():
  print "*" * 60
  print "Usgae: python Grep.py <filename> <word>"
  print "*" * 60

def grep():
  with open(sys.argv[1]) as file:
    for line in file:
      if re.search(sys.argv[2],line):
        print line,

def main():
  try:
    grep()
  except IndexError:
    banner()


if __name__ == '__main__':
  main()

