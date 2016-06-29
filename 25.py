import time

start = time.time()

def fibbo(n):
	if n == 1:
		return 1	
	elif n == 2:
		return 1
	else:
		return fibbo(n-2) + fibbo(n-1)


i = 4782
while True:
	if len(str(fibbo(i))) > 1000:
		print i
		break

elapsed = time.time() - start

print elapsed
