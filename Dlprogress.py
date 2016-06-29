#!/usr/bin/env python

import os,sys,getopt
import urllib,time

def Usage():
  print "usage: ./dlprogress.py <url> <url2>...."

def main(argv):
  try:
    opts,args = getopt.getopt(argv,"h")
  except getopt.GetoptError:
    Usage()
    sys.exit(2)

  for opt,arg in args:
    if opt in ("-h"):
      Usage()
      sys.exit(2)

  if len(args) < 1:
    Usage()
    sys.exit(2)

  i = 1
  for url in args:
    print "Downloading.....",url
    try:
      urllib.urlretrieve(url,str(i),reporthook=dlprogress)
    except:
      print "Error during the downloading...",url
    i += 1

def dlprogress(count,blocksize,totlasize):
  percent = (count * blocksize * 100 / totalsize)
  sys.stdout.write("%2d%%",percent)
  sys.stdout.write("\b\b\b")
  sys.stdout.flush()

if __name__ == '__main__':
  main(sys.argv[1:])

