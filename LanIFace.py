#!/usr/bin/env python

import os,sys
import sh

print sh.ifconfig("eth0")

sh.firefox("google.com")


