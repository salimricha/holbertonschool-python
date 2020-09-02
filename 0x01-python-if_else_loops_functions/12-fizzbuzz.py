#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(1, 101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            i = print("FizzBuzz", end=" ")
            continue
        elif fizzbuzz % 3 == 0:
            i = print("Fizz", end=" ")
            continue
        elif fizzbuzz % 5 == 0:
            i = print("Buzz", end=" ")
        continue
        else:
            i = print(fizzbuzz)
    return i
