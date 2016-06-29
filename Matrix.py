#!/usr/bin/env python


import os,sys



def main():
  matrix = {}
  n = int(raw_input())
  for m in xrange(n):
      count = 0
      r,c = [int(x) for x in raw_input().split()][0:2]
      for i in xrange(1,r+1):
          matrix[i] = list()
          for j in raw_input():
              matrix[i].append(int(j))
  print matrix

main()
