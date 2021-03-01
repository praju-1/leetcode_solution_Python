#!usr/bin/env python3
""" Count the number of prime numbers less than a non-negative number, n."""
def count_primes(n):
    """
      :type n: int
      :rtype: int
    """
    count = 0
    """ It is false for n+1 number """
    primes = [False for i in range(n+1)]
    """ looping upto limit n """
    for i in range(2,n):
        if primes[i] == False:
            count+=1
            j = 2
            while j*i<n:
                primes[j*i] == True
                j+=1
    return count

if __name__ == "__main__":
    n = int(input(" Enter number: "))
    prime = count_primes(n)
    print(" Total prime numbers are : ", prime)
