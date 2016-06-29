#!/usr/bin/env python

import re
import os
import sys

def main(word):
    with open("/var/log/messages","r") as file:
      for line in file:
        if re.search(line,word):
          print line


if __name__ == '__main__':
  main(sys.argv[1])
  


