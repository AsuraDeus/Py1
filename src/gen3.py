#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fractions import Fraction

def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a+b

def Phi():
    x = fib()
    a = next(x)
    for b in x:
        yield Fraction(b,a)
        a = b


# for k, f in zip(range(0,100), fib()):
#     print(f)

for k, f in zip(range(0,100), Phi()):
    print(f)
