
mx,mod = 1000013,1000003
arr = [0] * mx
arr[0] = 1
for i in xrange(1,mx):
    arr[i] = i * arr[i-1]
    arr[i] %= mod

tc = int(raw_input())
while tc > 0:
    tc = tc -1
    n,a = map(int,raw_input().split())
    if n >= mx:
        print 0
    else:
        a %= mx
        calc =arr[n] * a
        calc %= mod
        print calc

