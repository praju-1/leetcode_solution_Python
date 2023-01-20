"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

"""
try:
    a = int(input("How many elements you want insert into list : \n"))
    l = []
    def create_list(ele : int):
        "This function create list by user input"
        try:
            for i in range(ele):
                s = int(input("Enter element to append :"))
                #append elements to the empty list
                new = l.append(s)
            print("\nCreated list is : ", l)
        
        except Exception as e:
            print(e)

    create_list(a)


    
    n = int(input("\nEnter number you want to add :")) 
    new_array  =[]

    def addToArrayForm(num: list, k: int):
        "This function will add number to array form"
        try:
            #this will join list to string
            s =''.join(map(str,l))

            #Perform addition with new element
            add = int(s) + n

            #For iteration convert into string
            final = str(add)
            
            #iteration through string and append into new list with converting into integer
            for i in final:
                f = new_array.append(int(i))
                
            print("\nArray after adding interge value to it : ", new_array)
        except Exception as e:
            print(e)

    addToArrayForm(l, n)
except Exception as e:
        print(e)