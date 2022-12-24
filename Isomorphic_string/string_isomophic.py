"""
Python program to check two strings are isomorphic or not.

Defination of isomorphic string : Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself

"""
try:
    s = input("Enter the first string : ")
    t = input("\nEnter the second string : ")
    def isomorphic_string(string1 : str, string2 : str):
        "This function return string is isomorphic or not"
        try:
            #iterating over both strings
            for i in range(0, len(s)):
                #create temporary variable to store value of both string
                temp1=string1[i]
                temp2=string2[i]
                #checking index value of both string
                if string1.index(temp1) != string2.index(temp2):
                    print("\nGiven strings is not isomorphic")
                    
            print("\nGiven strings is isomorphic")
        
        except Exception as e:
            print(e)
            
    isomorphic_string(s, t)
    
except Exception as e:
    print(e)