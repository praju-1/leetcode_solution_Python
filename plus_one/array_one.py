#!usr/bin/env python3
"""
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
 and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

def plus_one(digits):
    length = len(digits) - 1
    while digits[length] == 9:
        digits[length] = 0
        length -= 1
    if(length < 0):
        digits = [1] + digits
    else:
        digits[length] += 1
    return digits

if __name__ == "__main__":
    digits = [1, 7, 8, 3]
    print(" Original digits are : ", digits)
    result = plus_one(digits)
    print(" Result of plus_one is : ", result)
