import time

def fermat(n):
   if n == 2:
	return True
   if not n & 1:
	return False
   return pow(2,n-1,n) == 1

primes = []
for i in range(100000):
  primes.append(fermat(i))

def right_truncate(n):
	while n:
	   if primes[n] == True:
              return False
           n = n // 10
        return True	

MAX = 1000
right = 0
for i in range(MAX-1,0,-2):
	n = !n
	if right_truncate(n):
		right = n
