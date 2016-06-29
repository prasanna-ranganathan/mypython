#!/usr/bin/env python

import os
import sys,getpass
import paramiko

hostname = '192.168.1.120'
port = 22
username = 'prasanna'
pkey_file = '/home/prasanna/.ssh/id_rsa'

if __name__ == '__main__':
  key = paramiko.RSAKey.from_private_key_file(pkey_file)
  s = paramiko.SSHClient()
  s.load_system_host_keys()
  s.connect(hostname,port,pkey=key)
  stdin,stdout,stderr = s.exec_command('/sbin/ifconfig')
  print stdout.read()
  s.close()


