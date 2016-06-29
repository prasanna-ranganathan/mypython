#!/usr/bin/env python

import os,sys
import urllib
import pynotify
from xml.etree.ElementTree import parse
from time import sleep


doc = parse('CricLiveScores.xml')

for item in doc.findall('item'):
  print item,
  title = int(item.findtext('title'))
  desc  = int(item.findtext('description'))
  print title,desc

