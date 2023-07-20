#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_numbers = [0, 1]
        for i in range(2, n):
            fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        return fib_numbers


# print(fibonacci_sequence(6))
# print(fibonacci_sequence(1))
# print(fibonacci_sequence(0))
# print(fibonacci_sequence(20))
