#!usr/bin/env python3
"""
Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
 without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
def is_subsequence(string1, string2, m, n):
    """ Base Cases """
    if m == 0:
        return True
    if n == 0:
        return False
    """ If last charactes are not matching """
    if string1[m-1] == string2[n-1]:
        return is_subsequence(string1, string2, m-1, n-1)

    """ If last characters are not matching """
    return is_subsequence(string1, string2, m, n-1)


if __name__ == "__main__":
    string1 = str(input(" Enter String1 : "))
    string2 = str(input(" Enter string2 : "))
    m = len(string1)
    n = len(string2)
    if is_subsequence(string1, string2, m, n):
        print(" Enter string1 is subsequence of string2 ")
    else:
        print(" Enter string1 is not subsequence of string2 ")

