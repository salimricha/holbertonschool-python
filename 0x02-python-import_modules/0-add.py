#!/usr/bin/python3
from add_0 import add


def add_import(a, b):
    print('{} + {} = {}'.format(a, b, add(a, b)))
add_import(1, 2)
