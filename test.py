#!/usr/bin/env python

import json
from bs4 import BeautifulSoup
import re
#import requests
import os,subprocess
from pprint import pprint


pat = re.compile(r'[0-9]+(?:\.[0-9]+){3}')

def main():
    with open('json_data.json','r') as file:
        data = json.load(file)

    soup = BeautifulSoup(str(data))
    ips = re.findall(pat,soup.text)
    ips.insert(0,"127.0.0.1") # for testing
    for ip in ips:
        try:
            cmd = subprocess.call(["ping","-c","3",ip])
            print cmd
        except:
            pass

main()
