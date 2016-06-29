#!/usr/bin/env python


import re

valid_email = []

def validEmail(email):
  if re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$",email) != None:
    return 1
  return 0


def main():
  t = int(raw_input())
  while t > 0:
    email = raw_input()
    if validEmail(email):
      valid_email.append(email)
    t = t - 1
  print sorted(valid_email)

main()
