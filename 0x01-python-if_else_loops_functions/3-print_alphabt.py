#!/usr/bin/python3
for alpha in range(97, 123):
    beta = chr(alpha)
    if beta not in "qe":
        print("{}".format(beta), end="")
