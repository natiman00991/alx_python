#!/usr/bin/env python3
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))
