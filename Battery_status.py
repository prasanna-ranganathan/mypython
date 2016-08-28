#!/usr/bin/python

import subprocess
import pynotify
import time

def status():
  command = "acpi | awk '{print $4}' | sed s/%,//"
  get_batterydata = subprocess.Popen(["/bin/bash", "-c", command], stdout=subprocess.PIPE)
  return get_batterydata.communicate()[0].decode("utf-8").replace("\n", "")

def Notification(title,message):
  pynotify.init("BatteryFull")
  notice = pynotify.Notification(title,message)
  notice.show()
  return

def Main():
  while True:
    if str(status()) == '100':
      Notification("Battery Full","100%  Unplug the charger")
    time.sleep(15)

if __name__ == '__main__':
  Main()

