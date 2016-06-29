#!/usr/bin/env python
import sys

class Calulator:
  def __init__(self, a, b):
      self.a = a
      self.b = b

  def add(self):
      return self.a + self.b
  def mul(self):
      return self.a * self.b

class Scentific(Calulator):
    def power(self):
      return pow(self.a,self.b)

Calculation = Calulator(int(sys.argv[1]),int(sys.argv[2]))

print 'a + b: ',Calculation.add()
print 'a * b: ',Calculation.mul()

print 'a** b: ',Scentific(10,20).power()
