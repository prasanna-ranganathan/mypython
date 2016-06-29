#!/usr/bin/env python

class Complex:
    def __init__(self,real,imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self,other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self,other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __div__(self,other):
        sr,si,orr,oi = self.real,self.imag,other.real,other.imag
        r = float(orr**2 + oi**2)
        return Complex((sr*orr+si*oi)/r, (si*orr-sr*oi)/r)

    def __mod__(self,other):
        return Complex(self.real % other.real,
                       self.imag % self.imag)


def main():
    x,y = map(int,raw_input().split())
    p,q = map(int,raw_input().split())
    a = complex(x,y)
    b = complex(p,q)
    resadd = Complex(a,b)
    ressub = Complex(a,b)
    resmul = Complex(a,b)
    resdiv = Complex(a,b)

    print resadd,ressub,resmul,resdiv

main()

