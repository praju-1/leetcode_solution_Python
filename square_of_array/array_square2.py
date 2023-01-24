"""
Python program return square of sorted array 

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

"""
try:
    #Initialize empty list
    s = []
    n = int(input("Enter how many numbers you want to enter :  "))
    def create_list(a : list):
        "This function used to add element to the list"
        try:
            print("\nOriginal list : ", a)
            for i in range(n):
                new = input("Enter item you want to append: ")
                a.append(new)
            print("\nList after appending element : ", a)
        except Exception as e:
            print(e)

    create_list(s)
    
    #initialize second empty list for insert square of array
    new = []
    def sortedSquares(nums: list, sorted_list : list):
        "This function return squared array of elements"
        try:
            #perform sorting
            x = nums.sort()
            print("sorted array : ", nums)
            #Convert string list into int list
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            
            #perform squaring and append to new list
            for i in range(len(nums)):
                sorted_list.append(nums[i]**2)
            print("Sorted Square of array is : ", sorted_list)
            
            
        except Exception as e:
            print(e)

    sortedSquares(s, new)
    
except Exception as e:
    print(e)