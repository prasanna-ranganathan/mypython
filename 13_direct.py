import time

start = time.time()

str = "

str = map(int,str.split("\n"))
s = sum(str)

elapsed = (time.time() - start)
print "found %s in %s seconds" % (s,elapsed)

