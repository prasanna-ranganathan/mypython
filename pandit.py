import sys
f = sys.stdin
mod = 1000000007

def gcd(a,b):

	if b==0:
		return a
	else :
		return gcd(b,a%b)


t = int(f.readline())
while t:
	a,b,c = [int(x) for x in f.readline().split()]
	g = gcd(a,gcd(b,c))
	v = (a*b*c)/(g**3)
	sys.stdout.write(str(g) + " " + str(v%mod) + '\n')
	t-=1

