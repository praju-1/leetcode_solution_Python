"""
Python program for missing number

Missing number : Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

"""

try:
    #assign empty list
    s = []
    #Taking input from user
    n = int(input("Enter how many numbers you want to enter :  "))

    def create_list(a : list):
        "This function used to add element to the list"
        try:
            print("\nOriginal list : ", a)
            for i in range(n):
                new = int(input("Enter item you want to append: "))
                #insert each number to the list
                a.append(new)
            print("\nList after appending element : ", a)
        except Exception as e:
            print(e)

    create_list(s)

    #initilize new list for appending missing number
    new_list = []
    def missing_number(number : list):
        "This function will return list of missing number"
        try:
            for i in range(number[0], number[-1]+1):
                #check for number in list
                if i not in number:
                    #missing number will append in new list
                    new_list.append(i)
            print("\nMissing number in list are : ", new_list)

        except Exception as e:
            print(e)

    missing_number(s)

except Exception as e:
    print(e)