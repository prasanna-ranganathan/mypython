#!/usr/bin/env python

import os,sys


def FindMissingArray(A,B):
  A.sort()
  B.sort()
  for num1,num2 in zip(A,B):
    if num1 != num2:
      return num1
  return A[-1]

import collections

def FindMissingNum2(A,B):
  d = collections.defaultdict(int)
  for num in B:
    d[num] += 1
  for num in A:
    if d[num] == 0:
      return num
    else:
      d[num] -= 1

def FindMissingNum3(A,B):
  result = 0
  for i in A + B:
    result ^= i
  return result

def main():
  A = [4,1,0,2,9,6,8,7,5,3]
  B = [6,7,4,2,1,0,8,3,9]
  print FindMissingArray(A,B)
  print FindMissingNum2(A,B)
  print FindMissingNum3(A,B)

if __name__ == '__main__':
  main()
