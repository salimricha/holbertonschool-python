#!/usr/bin/python3
import hidden_4


def hidden(str):
    for i in dir(str):
        if i[0] != "_":
            print(i, end="\n")
if _name_ == "_main_":
    hidden(hidden_4)
