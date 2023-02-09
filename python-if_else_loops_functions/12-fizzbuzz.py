#!/usr/bin/python3
def fizzbuzz():
for n in range(0, 101):
    if n % 3 == 0 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
    elif n  % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print("{}").format(n), end="")
