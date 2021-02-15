#!usr/bin/env python3
"""
Description:
    Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in the array,
    and it should return false if every element is distinct.
"""
def check_duplicate(array, n, k):
    """ Returns the boolean result for duplicate numbers.
        Parameters :
            array : list(int)
                contain list of integers
            n     : int
                length of array
            k     :  int
                The number for checking
    """
    """ Create an empty list """
    my_list = []

    """ Traverse the input array """
    for num in range(n):
        """ If already present n hash, then we
            found a duplicate within k distance
        """
        if array[num] in my_list:
            return True

        my_list.append(array[num])
        """ Remove the k+1 distant item """
        if num >= k:
            my_list.remove(array[num - k])
    return False

if __name__ == "__main__":
    array = [4, 3, 1, 3, 6, 7, 8]
    print(" The given array is", array)
    k = int(input(" Enter the number want to check : " ))
    n = len(array)
    if check_duplicate(array, n , k):
        print(" True ")
    else:
        print(" False ")
