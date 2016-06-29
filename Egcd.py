#!/usr/bin/python

import os,sys

def egcd(a,b):
  if a == 0:
    return (b,0,1)
  else:
    g,y,x = egcd(b % a,a)
    return (g,x - (b // a) * y,y)

def modinv(a,m):
  gcd,x,y = egcd(a,m)
  if gcd != 1:
    return None
  else:
    return x % m

def main():
  a = int(raw_input())
  b = int(raw_input())
  print egcd(a,b);
  m = int(raw_input())
  print modinv(a,m)


if __name__ == '__main__':
  main()
