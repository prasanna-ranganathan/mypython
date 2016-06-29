import sys
import time


def collatz_length(n,count=1):
	count += 1
	while n != 1:
	  if n % 2 == 0:
	    n = n / 2
	  else:
	    n = 3 * n + 1
	return count

def main():
	max = [0,0]
	for i in range(1000000):
	  _length = collatz_length(i)
	  if _length > max[0]:
	     max[0] = _length
	     max[1] = i 

	print "Starting Number is ",max[1],"Sequence",max[0]


if __name__ == '__main__':
	start = time.time()
	print "Starting......"
	main()
	elapsed = time.time() - start
	print "Ending!!"
	print "elapsed time is ",elapsed
