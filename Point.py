#!/usr/bin/env python

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point (%s,%s)" % (self.x,self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

