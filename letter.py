import time
import sys

num2words = { 1:'One', 2:'Two', 3:'Three', 4:'Four' , 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine',10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen' \
		,14:'Fourteen',15:'Fifteen',16: 'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty', \
		 60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'Hundred',1000:'Thousand',0:'zero' }

def number2words(n):
	if 1 <= n <	
	print num2words[n]
	except KeyError:
		try:
			print num2words[n-n%10] + num2words[n%10].lower()
		except KeyError:
			print 'Fuck You'






number2words(input())
