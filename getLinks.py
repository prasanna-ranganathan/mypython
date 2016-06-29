#!/usr/bin/env python

import urllib2,htmllib,formatter
import sys

def getLinks():
    website = urllib2.urlopen("http://www.profmcmmillan.com")
    data = website.read()
    website.close()
    Format = formatter.AbstractFormatter(formatter.NullWriter())
    ptext = htmllib.HTMLParser(Format)
    ptext.feed(data)
    for link in ptext.anchorlist:
        print link



if __name__ == '__main__':
    getLinks()



