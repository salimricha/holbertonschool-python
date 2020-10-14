#!/usr/bin/python3
import math


def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def factors(n):
    if isprime(n):
        return [n]
    L = []
    mn = 2
    mx = int(math.sqrt(n)+1)
    n1 = n
    repeat = True
    while(repeat):
        repeat = False
        for i in range(mn, mx):
            if n1 % i == 0:
                L.append(i)
                mn = i
                mx = int(math.sqrt(n1)+1)
                n1 = n1/i
                repeat = True
                break
    if n1 == 1:
        return L
    else:
        L.append(int(n1))
        return L


def primefactors(lst):
    return sorted(list(set(lst)))


def powerfactors(lst):
    a = primefactors(lst)
    pf = []
    for i in a:
        pf.append(lst.count(i))
    return pf


def minOperations(n):
    if n < 2 or n != int(n):
        return 0
    lst = factors(n)
    a = primefactors(lst)
    b = powerfactors(lst)
    s = 0
    for c in zip(a, b):
        s = s+c[0]*c[1]
    return s
