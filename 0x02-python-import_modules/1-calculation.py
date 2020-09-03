#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def import_add(a, b):
    print('{} + {} = {}'.format(a, b, add(a, b)))


def import_sub(a, b):
    print('{} - {} = {}'.format(a, b, sub(a, b)))


def import_mul(a, b):
    print('{} * {} = {}'.format(a, b, mul(a, b)))


def import_div(a, b):
    print('{} / {} = {}'.format(a, b, div(a, b)))
if _name_ == '_main_':
    a = 10
    b = 5
    import_add(a, b)
    import_sub(a, b)
    import_mul(a, b)
    import_div(a, b)
