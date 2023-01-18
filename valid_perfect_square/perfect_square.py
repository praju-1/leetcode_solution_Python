"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

"""
try:
    n = int(input("Enter number to check perfect square : "))
    def perfect(num : int):
        "This function return checks perfect square number"
        try:
            #divide number into two parts
            if int(num**0.5)*int(num**0.5)==num:
                return True
            else:
                return False
        except Exception as e:
            print(e)
    
    print("Given number is perfect square: ", perfect(n))

except Exception as e:
    print(e)