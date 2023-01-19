"""
Python program to return index to form target integer.

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

"""

try:
    n = [2,7,11,15]
    t = int(input("\nEnter the target value you want : "))
    
    def two_sum(num : list,  target : int):
        "This function return index of target value"
        try:
            #initalize empty dictionary
            dict = {}
            for i in range(len(num)):
                #store number in variable
                x = num[i]
                if target-x in dict:
                    return (dict[target-x], i)
                dict[x] = i
            print(dict)
        except Exception as e:
            print(e)

    print(two_sum(n , t))

except Exception as e:
    print(e)