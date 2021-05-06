#!usr/bin/env python3
"""
A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

def isHappyNumber(n):    
    digit = sum = 0    
    while(n > 0):    
        digit = n % 10 
        sum = sum + (digit * digit)    
        n = n // 10   
    return sum    

if __name__ == "__main__":
    num = int(input("Enter a number: "))    
    result = num    
    """ If the inputted number is 1 or 4 we don’t need to use isHappyNumber().
    because 1 is already happy number and if it is 4 then it is going to end in an endless cycle""" 
    while(result != 1 and result != 4):
        result = isHappyNumber(result)   
     
    if(result == 1):    
        print(num, " is a Happy Number!!!")   
    else:    
        print(num, " is an Unhappy Number!!!")
    