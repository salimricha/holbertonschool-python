#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        return None
    finally:
        print('{:d}'.format(c))
