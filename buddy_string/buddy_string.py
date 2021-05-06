#!usr/bin/env python3
"""
Given two strings A and B of lowercase letters, return true if you can swap two letters 
in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) 
such that i != j and swapping the characters at A[i] and A[j]. 
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

"""
def buddy_string(str1, str2):
    """
        :type str : string
        :rtype : Bool
    """

    """ If length is not equal then return False. """
    if (len(str1) != len(str2)):
        return False
    elif sorted(str1) != sorted(str2):
        return False
    elif str1 == str2 and len(set(str1)) == len(str1):
        return False
    else:
        count = 0
        """ Iterate through string. Check the differences. 
        The different letter can’t larger than 2 """
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                count += 1
                if count == 3:
                    return False
        return True

if __name__ == "__main__":
    str1 = str(input(" Enter string1 : "))
    str2 = str(input(" Enter string2 : "))
    print(buddy_string(str1, str2))
