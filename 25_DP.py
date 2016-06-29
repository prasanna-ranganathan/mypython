import time

start = time.time()

def fib(n):
	fibvalue = [0,1]
	for i in range(2,n+1):
		fibvalue.append(fibvalue[i-1] + fibvalue[i-2])
	return fibvalue[n]

print len(str(fib(4782)))

i = 100

while True:
	i += 1
	if len(str(fib(i))) == 1000:
		print i
		break

elapsed = time.time() - start
print elapsed
