#!/usr/bin/env python

import requests
import BeautifulSoup
from time import sleep

url = "http://static.cricinfo.com/rss/livescores.xml"

while True:
  r = requests.get(url)
  while r.status_code is not 200:
    r = requests.get(url)
  soup = BeautifulSoup.BeautifulSoup(r.text)
  data = soup.find_all("description")
  print "West Indices: ",data[1].text
  print "Australia:",data[2].text
  print "Delhi Daredevils:",data[3].text
  sleep(60)

