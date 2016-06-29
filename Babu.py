#http://ideone.com/bOxFqJ
#http://stackoverflow.com/questions/4223313/finding-abc-mod-m
def totient(n) :
    result = 1
    p = 2
    while p**2 <= n :
        if(n%p == 0) :
            result *= (p-1)
            n /= p
        while(n%p == 0) :
            result *=  p
            n /= p
        if p==2:
        	p += 1
        else:
        	p += 2
    if n != 1 :
        result *= (n-1)
    return result

def modpow(p, z, b, c, m) :
    if m == 2:
        return p % m
    cp = 0
    while m % p == 0 :
        cp += 1
        m /= p
    t = totient(m)
    exponent = ((pow(b,c,t)*z)%t + t - (cp%t))%t
    return pow(p, cp)*pow(p, exponent, m)
from fractions import gcd
def solve(a,b,c,m) : #split
    result = 1
    p = 2
    while p**2 <= a :
        cp = 0
        while a%p == 0 :
            a /= p
            cp += 1
        if cp != 0 :
           temp =  modpow(p,cp,b,c,m)
           result *= temp
           result %= m
        p += 1
    if a != 1 :
        result *= modpow(a, 1, b, c, m)
    return result % m
T = input()
#print pow(0,0,1)
import sys
for i in xrange(T):
	m1,n1,m2,n2,n = map(int,sys.stdin.readline().split())
	x = pow(m1,n1,n)
	if n==1:
		print 0
		continue
	if x==1:
		print 1
		continue


	else:

		if m2 < 10**2 and n2 < 10**1:
			y = pow(m2,n2)
			print pow(x,y,n)
			continue
		if x == 0:
			print 0
			continue
		print solve(x,m2,n2,n)

