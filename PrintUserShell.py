#!/usr/bin/python

from __future__ import print_function
import pwd


def getusers():
	Users = pwd.getpwall()
	for user in Users:
		print('{0}:{1}'.format(user.pw_name,user.pw_shell))
	

if __name__ == '__main__':
	getusers()

