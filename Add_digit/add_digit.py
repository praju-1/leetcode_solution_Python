"""
Python program for repeatedly add all its digits until the result has only one digit, and return it.

"""
try:
    n = int(input("Enter any number : "))
    def add_digit(num : int):
        "This function will return single number after addition"
        try:
            digit = 0
            #Checking for if number is greater
            while num > 0:
                #number will add and return reminder of num
                digit += num % 10
                #rounds the result down to the nearest whole number
                num = num // 10
            
                if num == 0 and digit > 9:
                    num = digit
                    digit = 0
            print("The last added digit is : ", digit)   
        except Exception as e:
            print(e)

    add_digit(n)
    
except Exception as e:
    print(e)