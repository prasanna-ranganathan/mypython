#!/usr/bin/env python

import sys
import paramiko
import getpass

hostname = '127.0.0.1'
port = 22
username = 'prasanna'
password = 'prasanna'

if __name__ == '__main__':
  paramiko.util.log_to_file('paramiko.log')
  s = paramiko.SSHClient()
#  s.load_system_host_keys()
  s.connect(hostname,port,username,password)
  stdin,stdout,stderr = s.exec_command('/sbin/ifconfig')
  print stdout.read()
  s.close()

