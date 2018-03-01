#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .inputkbd import input_kbd


def arrived_kbd():
    while True:
        sp = input_kbd()
        if not sp:
            break
        yield sp
