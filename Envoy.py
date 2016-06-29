#!/usr/bin/python

import os,sys
import envoy

cmd = ['date','uptime','df -h']

for i in cmd:
    r = envoy.run(i)
    print r.status_code,r.std_out


