#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import start


best = dict()

for result, familia in start.arrived_kbd():
    best[result].append((result, familia))
