import time

count = 0
def collatz_length(n):
	while n:
		++count
		if n & 1:
			n = 3 * n + 1
		else:
			n = n >> 2
	return count

print collatz_length(input())
