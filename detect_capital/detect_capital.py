#!usr/bin/env python3

"""Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way. """

def detect_capital(word):
    """
        :type word: str
        :rtype: bool
    """
    n = len(word)
    if len(word) == 1:
        return True
   
    # case 1: All capital
    if word[0].isupper() and word[1].isupper():
        for i in range(2, n):
            if not word[i].isupper():
                return False
    # case 2 and case 3
    else:
        for i in range(1, n):
            if word[i].isupper():
                return False
   
    # if pass one of the cases
    return True
    
if __name__== "__main__":
    word = str(input(" Enter the string for detection : "))
    print(" Enter word is : ", word)
    result = detect_capital(word)
    print(result)
