#!/usr/bin/python3
from add_0 import add


def import_add(a, b):
    print('{} + {} = {}'.format(a, b, add(a, b)))
if _name_ == '_main_':
    a = 1
    b = 2
    import_add(a, b)
