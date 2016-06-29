#!/usr/bin/env python

def Doit(num):
    length = len(str(num))
    oddDigits = (length % 2 != 0)
    lefthalf = getleft(num)
    middle = getmiddle(num)
    if oddDigits:
        increment = pow(10,length/2)
        newNum = int(lefthalf+middle+lefthalf[::-1])
    else:
        increment = int(1.1 * pow(10,length/2))
        newNum = int(lefthalf+lefthalf[::-1])
    if newNum > num:
        return newNum
    if middle != '9':
        return newNum+increment
    else:
        return Doit(Roundup(num))


def getleft(num):
    return str(num)[:len(str(num))/2]

def getmiddle(num):
    return str(num)[(len(str(num))-1)/2]

def Roundup(num):
    length = len(str(num))
    increment = pow(10,(length/2)+1)
    return ((num/increment) + 1) * increment


print Doit(input())
