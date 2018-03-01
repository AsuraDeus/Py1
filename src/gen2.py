#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def primes():
    n = 2
    while True:
        for k in range(2,n):
            if n % k == 0:
                break
        else:
            yield n
        n += 1
for p in primes():
    print(p)
