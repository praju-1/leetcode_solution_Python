#!usr/bin/env python3
"""
A perfect number is a positive integer that is equal to the sum of its positive divisors, 
excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

"""
def perfect_num(n):
    """
    :type n : int
    :rtype : bool
    """
    """ To store sum of divisors """
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum = sum + i
    """ If sum of divisors are equal to n, then n is perfect number"""
    return (True if sum == n and n != 1 else False)

if __name__ == "__main__":
    n = int(input(" Enter number : "))
    print(" The entered number is : ", n)
    if (perfect_num(n)):
        print(" Entered number is perfect number ")
    else:
        print(" Entered number is not perfect number ")