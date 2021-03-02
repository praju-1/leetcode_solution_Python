"""
Description:
Given two strings s and t, check if str1 is a subsequence of str2.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters
 without disturbing the relative positions of the remaining characters.
"""

""" Returns true if str1 is a subsequence of str2 """

def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0    # Index of str1
    i = 0    # Index of str2

    """ Traverse both str1 and str2
    Compare current character of str2 with
    first unmatched character of str1
    If matched, then move ahead in str1 """

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1

    """If all characters of str1 matched,
    then j is equal to m """
    return j == m

if __name__ == "__main__":
    str1 = str(input(" Enter String1 : "))
    str2 = str(input(" Enter string2 : "))

    if isSubSequence(str1, str2):
        print(" Given string is subsequence of other ")
    else:
        print(" Given string is not subsequence of other ")
