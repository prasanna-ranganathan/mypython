import time
import math

start = time.time()

def digit():
	l = 1
	while l <= 100000:
		i = sum(range(l+1))
		yield i
	 	l = l+1

for i in digit():	
	count = 0
	for j in range(1,int(math.sqrt(i) + 1)):
		if i % j == 0: 
			count += 1

	if count * 2 > 500:
		print i,count
		break

elapsed = time.time() - start
print elapsed
