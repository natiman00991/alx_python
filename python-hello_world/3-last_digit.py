#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
num = number
if num < 0:
    num = num * -1
else:
    pass

last_digit = num % 10
ddd = -1 * last_digit

if last_digit > 5 and number >= 0:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0 and number >= 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {ddd} and is less than 6 and not 0")
