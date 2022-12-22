"""
Given two non-negative integers, num1 and num2 represented as string, 
return the sum of num1 and num2 as a string.

"""

try:
    num1 = input("Enter integer to add : ")
    num2 = input("Enter second integer to add  :")
    def add_string(x, y):
        """
        This function return addition of string
        :type num1: str
        :type num2: str
        :rtype: str
        """
        try:
            sum = int(x) + int(y)
            a = str(sum)

            print("Addition of two integer is : ", a)
        
        except Exception as e:
            print(e)

    add_string(num1, num2)

except Exception as e:
    print(e)