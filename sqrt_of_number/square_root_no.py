"""
Python program for return square root of given number

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

Without using any built-in function
"""
try:
    n = int(input("Enter number to return its square root :"))
    def square_root_of_number(num : int):
        "This function return the square root of the number"
        try:
            x = int(num**0.5)
            print("\nSquare root of given number is : ", x)
        except Exception as e:
            print(e)
    square_root_of_number(n)      
except Exception as e:
    print(e)