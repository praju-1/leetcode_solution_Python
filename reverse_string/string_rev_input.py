"""
Python program for reversing string.

Write a function that reverses a string. The input string is taken from user.
"""

try:
    s = []
    n = int(input("Enter how many string you want to enter :  "))
    def create_list(a : list):
        "This function used to add element to the list"
        try:
            print("\nOriginal list : ", a)
            for i in range(n):
                new = input("Enter item you want to append: ")
                a.append(new)
            print("\nList after appending element : ", a)
        except Exception as e:
            print(e)

    create_list(s)

    def reverse_string(element : list):
        "This function return reverse string"
        try:
            print("Original string is : ", element)

            p = element[::-1]

            print("The reverse string is : ", p)

        except Exception as e:
            print(e)
    reverse_string(s)
except Exception as e:
    print(e)