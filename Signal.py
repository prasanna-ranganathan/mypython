#!/usr/bin/env python

import signal

def ctrlc_handler(signum,frm):
    print "Haha You cannot kill me!"


print "Installing signal Handler"
signal.signal(signal.SIGINT, ctrlc_handler)

print "Done"

while True:
    pass
