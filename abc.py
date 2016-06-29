def abc(prefix,string):
   N = len(string)
   if N == 0: print prefix
   else:
       for i in range(0,N):
	   print "Before: ",(i,string,prefix+string[i],string[0:i] + string[i+1:N])
           abc(prefix+string[i],string[0:i]+string[i+1:N])
           print "After: ",(i,string,prefix+string[i],string[0:i] + string[i+1:N])
	  
abc("","abc")
