#!/usr/bin/env python

import os,sys

matrix = []

def main():
    n,m = map(int,raw_input().split())
    row = map(int,raw_input().split())
    matrix.append(row)

    for i in xrange(n):
        for j in xrange(m):
            print matrix[i][j]


main()
