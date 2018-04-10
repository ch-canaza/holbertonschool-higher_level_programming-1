#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is".format(number), end = " ")

if number > 0:
    print("{:d}".format(number % 10), end = " ")
else:
    print("-{:d}".format((number * -1) % 10), end = " ")

if number % 10 == 0:
    print("and is 0")
elif number < 0:
    print("and is less than 6 and not 0")
elif number % 10 > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
