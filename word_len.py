import time
import sys

unit_names = """zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen""".split()

tens_names = """zero ten twenty thirty forty fifty sixty seventy eighty ninety""".split()

def words(n):
	if n >= 1000:
	  thous = words(n // 1000) + "thousand"
	  n = n % 1000
	  if n == 0:
		return thous
	  elif n < 100:
		return thous + " and " +  words(n)
	  else:
		return thous + ", " + words(n)
	elif n>=100:
	  huns = unit_names[n // 100] + "hundred"
	  n = n % 100
	  if n == 0:
		return huns
	  else:
		return huns + " and " + words(n)
	elif n >= 20:
	 tens = tens_names[n // 10]
	 n = n % 10
	 if n == 0:
	    return tens
	 else:
	    return tens + "-"+ words(n)
	else:
	    return unit_names[n]

def counts(s):
# Regular expression 
	import re
	return len(re.findall(r'[a-zA-Z]',s))

def main():
#	count = 0
#	for i  in range(1,1001):
#	 count  += len(words(i))
#	print count
	print sum(counts(words(i)) for i in range(1,1001))
	
if __name__ == '__main__':
	main()
#print words(input())
