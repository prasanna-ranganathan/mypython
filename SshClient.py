#!/usr/bin/env python

import os,sys
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(sys.argv[1],username=sys.argv[2],password='prasanna')
stdin,stdout,stderr = ssh.exec_command("sudo fdisk -l")
for i in stdout.readlines():
    print i,
ssh.close()
