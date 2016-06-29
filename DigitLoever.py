#!/usr/bin/python

def lover(x,y):
    z = ''
    for i,j in zip(x,y):
        z += str(int(i) + int(j))
    print z
    z += y[len(x):]
    return z
    
def main():
    T = int(raw_input())
    while T  > 0:
      s1,s2 = map(str,raw_input().split())
      if len(s1) <= len(s2):
      	x,y = s1,s2
      else:
      	y,x = s1,s2
      print lover(x,y)
      T -= 1

main()
