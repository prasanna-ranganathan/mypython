#!/usr/bin/python

name = raw_input("Enter your Name: ")

print "Your Nmae is " + name

if name == "Prasanna":
    print "Your are Prasanna"
    print "Normal User"
elif name == 'root':
    print 'Your are root'
    print "Linux Admin"
else:
    print "Unknown user"
