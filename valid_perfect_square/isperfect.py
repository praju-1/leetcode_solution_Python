"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

"""
try:
    n = int(input("Enter number to check perfect square : "))
    def perfect(num : int):
        "This function return checks perfect square number"
        try:
            if num == 1:
                return True
            
            # Go through each number
            # And check if its square is equal to num
            for i in range(1, num + 1):
                if i * i == num: 
                    return True
            
            # Not a perfect square
            return False
           
        except Exception as e:
            print(e)
    
    print("Given number is perfect square: ", perfect(n))

except Exception as e:
    print(e)