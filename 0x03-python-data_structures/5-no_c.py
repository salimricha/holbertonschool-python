#!/usr/bin/python3
def no_c(my_string):
    c_chars = ['c', 'C']
    my_string = filter(lambda i: i not in c_chars, my_string)
    test_string = ''.join(i for i in my_string if i not in c_chars)
    return test_string
