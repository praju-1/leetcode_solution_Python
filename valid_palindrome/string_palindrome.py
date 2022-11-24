"""
Python program for check given string is valid palindrome or not.

Defination of palindrome string : A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
 Alphanumeric characters include letters and numbers.

"""
#importing regular expression
import re
try:
    n = input("Enter string to check :")
    def palindrome_string(string : str):
        "This function check string is palindrome or not"
        try:
            print("\nEntered string to check : ", string)
            # this check for similar string format
            if string == string[::-1]:
                print("\nGiven string is palindromic string")
                
                # if string is upper or in title format it will convert it into lower case then reverse it.
            elif string.isupper() or string.istitle():
                x = string.lower()
                x == x[::-1]
                print("\nGiven string is palindromic string")
                
                #below we removes all non-alphanumeric characters from string.
            elif string.isalpha() == False or string.isalnum() == False:
                # here we use regular expression
                s = re.sub(r'[^a-zA-Z0-9]', '', string)
                s == s[::-1]
                print("\nGiven string is palindromic string")
            else:
                print("\nGiven string is not palindromic string")
        except Exception as e:
            print(e)
        
    palindrome_string(n)

except Exception as e:
    print(e)