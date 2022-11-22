"""
Python program to check enter number is palindrome or not.

Defination of Palindrome : A palindromic number is a number that remains the same when its digits are reversed

"""
try:
    n = input("Enter any number :")
    def palindrome(item : int):
        "This function check number is palindrome or not"
        try:
            print("\nEntered number is : ", item)
            if item == item[::-1]:
                print("\nGiven number is palindromic number")
            else:
                print("\nGiven number is not palindromic number")
        except Exception as e:
            print(e)
        
    palindrome(n)
except Exception as e:
    print(e)