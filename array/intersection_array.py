#!usr/bin/env python3
"""
Description:
Two array are given. we have to compute their intersection.
"""
def intersection(array1, array2):
    """
      :type array1: List[int]
      :type array2: List[int]
      :rtype: List[int]
    """
    array = {}

    """ Comparing length of array """
    if len(array1) < len(array2):
        """ If length of array1 is smaller than array2 then swap them """
        array1, array2 = array2, array1

    """ Iterate through array1 for checking element """    
    for i in array1:
        if i not in array:
            array[i] = 1
        else:
            array[i] += 1
    """ Initialize empty list for result of intersection """
    result = []

    """ Iterate through array2 for checking element """ 
    for i in array2:
        if i in array and array[i]:
            array[i] -= 1
            result.append(i)
    return result

if __name__ == "__main__":
    array1 = [1, 3, 4, 6, 5, 3, 6]
    array2 = [1, 2, 4, 6, 7, 8, 9]
    print(" Array 1 is : ", array1)
    print(" Array 2 is : ", array2)
    result = intersection(array1, array2)
    print(" Intersection of arrays is :", result)
