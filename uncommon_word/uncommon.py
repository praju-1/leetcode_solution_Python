#!usr/bin/env python3

"""
We are given two sentences A and B.

A word is uncommon if it appears exactly once in one of the sentences, 
and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.

"""
def uncommon_word(str1, str2):
    """ Initialize empty string """
    re = ""
    """ Spliting sentences """
    a = str1.split()
    b = str2.split()
    """ Iterate through sentence and check uncommon word in another sentence"""
    for i in a:
        if i not in b:
            """ Concate the string """
            re = re+" "+i
    
    for j in b:
        if j not in a:
            re = re+" "+j
    return re

if __name__ == "__main__":
    str1 = " this apple is sweet "
    str2 = " this apple is sour "
    print(" str1 is : ", str1)
    print(" str2 is : ", str2)
    print(uncommon_word(str1, str2))
