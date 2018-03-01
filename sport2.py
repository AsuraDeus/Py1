#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import start


best = []
for sp in start.arrived_kbd():
    best.append(sp)
    best.sort()
    if len(best) > 5:
        del best[-1]
    for result, familia in best:
        print('{0} -- {1}'.format(result, familia))
        # print(f'{result:2f} -- {familia}') -- 3.6py
