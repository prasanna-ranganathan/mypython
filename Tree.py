#!/usr/bin/env python

import os,sys

def banner():
  print '*' * 60
  print 'Usage: python Tree.py <dir>'
  print '*' * 60

filecount = 0

def tree(filepath):
  path = os.path.abspath(filepath)
  for filename in os.listdir(filepath):
    filepath = os.path.join(path,filename)
    if os.path.isfile(filepath):
      filecount += 1
      print '--',filepath
    elif os.path.isdir(filepath):
      tree(filepath)

def main():
  try:
    tree(raw_input())
  except:
    banner()

if __name__ == '__main__':
  main()
