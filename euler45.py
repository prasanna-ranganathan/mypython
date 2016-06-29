import time
import math


def is_pentagonal(n):
   return (1 + math.sqrt(1 + (24 * n))) % 6 == 0

def hexa(n):
  return (n * (2 * n - 1) )

i = 40755
hexa1 = (1 + math.sqrt(1 + ( 8 * 40755))) / 4

while True:
   hexa1 += 1
   num = hexa(hexa1)
   if is_pentagonal(num):
	print int(num)
	break


