"""
Your friend is typing his name into a keyboard. Sometimes, 
when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
"""
try:
    value  = input("Enter any string : ")
    value1 = input("Enter another string : ")
    def long_pressed(name : str, typed : str):
        "This function return true if string is get long pressed"
        try:
            count = 0
            for i in range(len(typed)):
                #it can verify with length of name
                if count < len(name) and  name[count] == typed[i]:
                    count += 1
                    
                elif i == 0 or typed[i] != typed[i - 1]:
                    return False
            return count == len(name)

        except Exception as e:
            print(e)


    print("Is entered string is long Pressed : ", long_pressed(value, value1 ))
except Exception as e:
    print(e)