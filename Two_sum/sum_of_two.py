"""
Python program to return index to form target integer.

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

"""

try:
    a = int(input("How many elements you want insert into list : "))
    l = []
    def create_list(ele : int):
        "This function create list by user input"
        try:
            for i in range(ele):
                s = int(input("Enter element to append :"))
                #append elements to the empty list
                new = l.append(s)
            print("Created list is : ", l)
        
        except Exception as e:
            print(e)

    create_list(a)

    t = int(input("\nEnter the target value you want : "))
    def two_sum(num : list,  target : int):
        "This function return index of target value"
        try:
            #initalize empty dictionary
            dict = {}
            for i in range(len(num)):
                #store number in variable
                x = num[i]
                #it check for value which is associte with target value
                if target-x in dict:
                    #return value to dictionary
                    return (dict[target-x], i)
                dict[x] = i
            print(dict)
        except Exception as e:
            print(e)

    print("Indexes of target value is : ", two_sum(l , t))

except Exception as e:
    print(e)