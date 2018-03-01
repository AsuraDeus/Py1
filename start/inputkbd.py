#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from decimal import Decimal


def dec2(result):
    return Decimal(result).quantize(Decimal('0.01'))


def input_kbd():
    familia = input('Фамилия: ')
    if familia == 'end':
        return None
    result = input('Результат: ')
    return (dec2(result), familia)
