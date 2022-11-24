"""
Python program for palindrome string.
"""


try:
    n = input("Enter string to check :")
    def palindrome_string(string : str):
        "This function check string is palindrome or not"
        try:
            print("\nEntered string to check : ", string)
            #It return string in lower case
            x = string.lower()

            # this check for similar string format
            if x == x[::-1]:
                print("\nGiven string is palindromic string")
                #it check for whitespaces in string
            elif string.isspace():
                # It remove spaces from string
                y = string.strip()
                y == y[::-1]
                print("\nGiven string is palindromic string")
            else:
                print("\nGiven string is not palindromic string")
        except Exception as e:
            print(e)
        
    palindrome_string(n)

except Exception as e:
    print(e)