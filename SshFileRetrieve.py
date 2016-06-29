#!/usr/bin/python

import sys
import paramiko
import getpass
import os

hostname = sys.argv[1]
port = 22
username = sys.argv[2]
password = getpass.getpass()
dirpath = '/home/prasanna/Python'

if __name__ == '__main__':
  t = paramiko.Transport((hostname,port))
  t.connect(username=username,password=password)
  sftp = paramiko.SFTPClient.from_transport(t)
  files = sftp.listdir(dirpath)
  for f in files:
    print "Retrieveing: ", f
    sftp.get(os.path.join(dirpath,f),f)
  t.close()

