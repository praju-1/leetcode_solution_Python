#!usr/bin/env python3
"""
Program for left-rotation in array
"""
def rotated_array(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    """ loop for rotation differnce is less than n"""
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(" Original array is : ", arr)
    print(" Array after left rotation is: ", end=' ')
    print(rotated_array(arr, len(arr), 2))  
