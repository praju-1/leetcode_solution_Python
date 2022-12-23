"""
Python program for string anagram.

Defination of Anagram : An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

"""
try:
    n = input("Enter string to check :")
    m = input("\nEnter another string : ")
    def valid_string_anagram(string1 : str, string2 :  str):
        "This function check string is anagram or not"
        try:
            # convert both the strings into lowercase
            string1 = string1.lower()
            string2 = string2.lower()
            
            #Checking length of both string
            if len(string1) == len(string2):
                #if length is same then we sort both the string
                sort_str1 = sorted(string1)
                sort_str2 = sorted(string2)
                
                #After sorting string we compare both string
                if sort_str1 == sort_str2:
                    print("\n", string1 + " and " + string2 + " are anagram.")
                else:
                    print("\n", string1 + " and " + string2 + " are not anagram.")
            
            else:
                print("\n" ,string1 + " and " + string2 + " are not anagram.")
                
        except Exception as e:
            print(e)

    valid_string_anagram(n, m)
except Exception as e:
    print(e)