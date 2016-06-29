#!/usr/bin/env python

import os,sys
import ConfigParser
import time

config = ConfigParser.ConfigParser()
config.read("/etc/mysql/debian.cnf")
username = config.get('client','user')
password = config.get('client','password')
hostname = config.get('client','host')


filestamp = time.strftime('%Y-%m-%d')

database_list_command = "mysql -u %s -p %s -h %s --silent -N -e 'show databases' " % (username,password,hostname)

for database in os.popen(database_list_command).readlines():
    database = database.strip()
    if database == 'Information_schema':
        continue
    if database == 'performance_schema':
        continue
    filename = "/basckups/mysql/%s-%s.sql" % (database,filestamp)
    os.open("mysqldump -u %s -p %s -h %s -e --opt -c %s | gzip -c > %s.gz" % (username,password,hostaname,database,filename))

