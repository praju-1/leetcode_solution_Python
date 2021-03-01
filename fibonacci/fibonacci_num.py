#!usr/bin/env python3
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""
def fibonacci_num(n):
    """Check if input is less than 0 then it will print incorrect input """
    if (n < 0):
        print("Incorrect input")
        """ Check if input is equal to 0 then it will return 0 """
    elif (n == 0):
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci_num(n-1) + fibonacci_num(n-2)

if __name__ == "__main__":
    n = int(input(" Enter the number : "))
    print(" The given number is : ", n)
    result = fibonacci_num(n)
    print(" The fibonacci number is : ", result)
