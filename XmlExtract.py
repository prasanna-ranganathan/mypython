#!/usr/bin/env python3

from urllib.request import urlopen
from xml.etree.ElementTree import parse

req = urlopen('http://planet.python.org/rss20.xml')
doc = parse(req)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date =  item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()


