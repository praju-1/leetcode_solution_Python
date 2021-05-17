#!usr/bin/env python3
"""
Description:
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
"""
def move_zeros(nums):
    """
      :type nums: List[int]
      :rtype: None Do not return anything, modify nums in-place instead.
    """
    """ Count all non-zero element """
    count = 0 
    
    """ Traverse the array. If element encountered is non-zero, then replace the element at index
    'count' with this element"""
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count]=nums[i]
            """ here count is incremented """
            count+=1

    """ Now all non-zero elements have been shifted to front and 'count' is set
    as index of first 0. Make all elements 0 from count to end."""
    for i in range(count,len(nums)):
        nums[i]=0

if __name__ == "__main__":
    nums = [1, 0, 0, 3, 4, 8, 0, 9, 0]
    print(" Original nums array is : ", nums)
    move_zeros(nums)
    print(" Modified array : ", nums)
