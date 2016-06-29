#!/usr/bin/env python

import re
import sys

def matchcase(word):
  def replace(m):
    text = m.group()
    print text
    if text.isupper():
      return word.upper()
    elif text.islower():
      return word.lower()
    elif text[0].isupper():
      return word.capitalize()
    else:
      return word
    return replace

def main():
  return re.sub('python',matchcase('snake'),sys.argv[1],flags=re.IGNORECASE)


main()
