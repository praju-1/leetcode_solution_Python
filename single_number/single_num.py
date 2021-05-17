#!usr/bin/env python3
"""Given a non-empty array of integers nums, every element appears twice except for one.
 Find that single one."""
"""Input: nums = [2,2,1]
Output: 1"""

def single_num(nums):
    """
       :type nums: List[int]
       :rtype: int
    """
    result = []
    """ Iterate through the list and perform append and remove operations. """
    for i in nums:
        if i not in result:
            result.append(i)
        else:
            result.remove(i)
    return result

if __name__ == "__main__":
    nums = [2, 2, 1, 3, 4, 4, 1]
    print(" The given list is : ", nums)
    output = single_num(nums)
    print(" Result is :",output)