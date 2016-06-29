#!/usr/bin/python


def power(a,b,mod):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 1:
            x = x * y
            if x > mod:
                x %= mod
        y = y * y
        if y > mod:
            y %= mod
        b /= mod
    return x

def Modinverse(a,m):
    return power(a,m-2,m)

def main():
    a,m = map(int,raw_input().split())
    print Modinverse(a,m)

if __name__ == '__main__':
    main()

