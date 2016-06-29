def nextHighNumber(num):
    strNum = str(num)
    length = len(strNum)
    for i in range(length-2,-1,-1):
	current = strNum[i]
	right   = strNum[i+1]
	if current < right:
	   temp = sorted(strNum[i:])
	   print temp
	   next = temp[temp.index(current)+1]
	   print next
	   temp.remove(next)
	   print temp
	   temp = ''.join(temp)
           print temp
           return int(strNum[:i]+next+temp)
    return num


print nextHighNumber(input())
