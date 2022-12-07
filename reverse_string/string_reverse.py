"""
Python program for reversing string.

Write a function that reverses a string. The input string is given as an array of characters s.
"""

try:
    s = ["h","e","l","l","o"]
    def reverse_string(element : list):
        "This function return reverse string"
        try:
            print("Original string is : ",element)
            p = element[::-1]

            print("The reverse string is : ", p)

        except Exception as e:
            print(e)
    reverse_string(s)
except Exception as e:
    print(e)