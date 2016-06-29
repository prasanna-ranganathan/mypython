def euler13():
	sum_num = 0
	with open("13.txt") as f:
	   for each in f:
	       sum_num += int(each)
	       print sum_num
	print (str(sum_num)[0:10])

