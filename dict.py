#!/bin/python

import json
import sys

with open("dictionary.json",'r') as file:
    try:
      parsed_json = json.load(file)
      print parsed_json[sys.argv[1]]
    except:
      print "No Such Word Exists"


