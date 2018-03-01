#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gen1():
    yield 1
    yield 3
    yield 5
    yield 7
    yield 9

x = gen1()
print(x)
print(next(x))
print(next(x))
print('---------')
for y in x:
    print(y)
