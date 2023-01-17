"""
Python program to find unique character from given string

condition : Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

"""

try:
    word = input("Enter string in which you want to find unique characters index : ")
    def first_unique_char(s : str):
        try:
            #iterate through string
            for i in range(len(s)):
                #count the character which occure only once
                if s.count(s[i])==1:
                    return i
            return -1
               
        except Exception as e:
            print(e)

    print("Index of unique character of word " + word + " is : ", first_unique_char(word))
except Exception as e:
    print(e)