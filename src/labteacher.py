#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import start

best = None

for sp in start.arrived_kbd():
    q = sp < best if best else True
    if q:
        best = sp
    print(best)
