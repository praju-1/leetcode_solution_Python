"""
Python program to convert number into hexadecimal form  using hex() function

"""

try:
    num = int(input("Enter number to convert : "))
    def to_hex(x : int):
        "This function return number to hexadecimal string"
        try:
            #Converting into hex
            result = hex(x)
            print("\nThe hexadecimal form of given number is :  ", result)

        except Exception as e:
            print(e)

    to_hex(num)
except Exception as e:
    print(e)