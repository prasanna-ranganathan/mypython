#!/usr/bin/env python

import hashlib
import sys

def Create_checksum(path):
  """
  reads in file.creates checksum of files line by line.
  """

  fp = open(path)
  checksum = hashlib.md5()
  while True:
    buffer = fp.read(8192)
    if not buffer: break
    checksum.update(buffer)
  fp.close()
  checksum = checksum.digest()
  return checksum

print Create_checksum(sys.argv[1])

