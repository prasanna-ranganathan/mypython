#!/usr/bin/env python

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')
office_lat = 41.980262

for bus in doc.findall('bus'):
  lat = float(bus.findtext('lat'))
  if lat >= office_lat:
    Bus_id = int(bus.findtext('id'))
    direction = bus.findtext('d')
    if direction.startswith('North'):
      print Bus_id,direction,lat
