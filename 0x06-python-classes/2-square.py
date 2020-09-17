#!/usr/bin/python3
'''this .....'''


class Square:
    def __init__(self, size=0):
        self.__size = size

    def size(self, value):
        if value.is_integer():
            self.__size = value
        else:
            raise TypeError
