#!/usr/bin/python
import sys,os

A = []
usr = raw_input()
fo = open('passwd','r')
for i in fo:
  A.append(i.split(":"))

print A
fo.close()
