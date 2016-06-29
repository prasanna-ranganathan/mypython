#!/usr/bin/env python

from collections import deque

def search(lines,pattern,history=5):
    p_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,p_lines
        p_lines.append(line)

if __name__ == '__main__':
    with open('access_log') as f:
        for line,p_lines in search(f,'HEAD',5):
            for pline in p_lines:
                print pline
            print line
            print '-' * 20


