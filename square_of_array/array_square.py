"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

"""
try:
    s = [12, 54, 2, 16, 10, 8]
    new = []
    def sortedSquares(nums: list, num1 : list):
        "This function return squared array of elements"
        try:
            #perform sorting using sort function
            x = nums.sort()
            print("List after sorting elements is : ", nums)
            #iterate through list
            for i in nums:
                new.append(i**2)
            print("Array of squaring each element : ", new)
        except Exception as e:
            print(e)

    sortedSquares(s, new)
    
except Exception as e:
    print(e)