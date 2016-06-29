#!/usr/bin/env python
import os,sys
import urllib
import re

url = "http://checkip.dyndns.org/"
print url

urlread = urllib.urlopen(url).read()
Ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1.3}",urlread)
print "My Ip: ",Ip
