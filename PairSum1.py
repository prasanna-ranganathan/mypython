#!/usr/bin/env python

def pairsum1(arr,k):
    if len(arr) < 2:
        return
    arr.sort();
    left,right = (0,len(arr)-1)
    while left < right:
        total = arr[left] + arr[right]
        if total == k:
            print arr[left],arr[right]
            left += 1
        elif total < k:
            left += 1
        else:
            right -= 1
arr = [1,2,1,3,4]
k = 4

pairsum1(arr,k)

