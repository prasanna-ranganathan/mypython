#!/usr/bin/env python


import os,sys

t = input()
while t > 0 :
    t = t - 1
    ans = 0
    n,m = map(int,raw_input().split())
    if m == 1:
        ans = n
    else:
        while n > 0:
            ans = ans + n % m
            n = n / m
    print ans

