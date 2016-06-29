#!/usr/bin/python

from __future__ import print_function
import pwd
import argparse
import os

def read_login_defs():

	Uid_Min = None
	Uid_Max = None
	
	if os.path.exists('/etc/login.defs'):
		with open('/etc/login.defs') as f:
			login_data = f.readlines()
		
		for line in login_data:
			if line.startswith('UID_MIN'):
				Uid_Min = int(line.split()[1].strip())
			
			if line.startswith('UID_MAX'):
				Uid_Max = int(line.split()[1].strip())
	
	return Uid_Min,Uid_Max

def getUsers(no_system=False):

	Uid_Min,Uid_Max = read_login_defs()

	if Uid_Min is None:
		Uid_Min = 1000
	if Uid_Max is None:
		Uid_Max = 60000
	
	Users = pwd.getpwall()
	for user in Users:
		if no_system:
			if user.pw_uid >= Uid_Min and user.pw_uid <= Uid_Max:
				print("{0}:{1}".format(user.pw_name,user.pw_shell))
		else:	
			print("{0}:{1}".format(user.pw_name,user.pw_shell))

if __name__ == '__main__':
		
		parser = argparse.ArgumentParser(description='User/Password utility')

		parser.add_argument('--no-system',action='store_true',dest='no_system',default = False, help='Specify to omit system users')
		
		args = parser.parse_args()
		getUsers(args.no_system)


