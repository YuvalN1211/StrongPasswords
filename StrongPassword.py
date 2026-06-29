def InputPassword():
    password = str(input("Enter your password: "))
    if(len(password) == 0):
        InputPassword()
    else:
        print("password selected")
        return password

def LengthCheck():
    global password
    print(f"my password is {password} from LengthCheck")
    if len(password) < 8:
        return 0
    elif len(password) < 12:
        return 1
    else:
        return 2

def ComplexityCheck():
    global password
    print(f"my password is {password} from ComplexityCheck")
    #defining starting values for booleans
    bool_dict = {"is_there_small_letters":False, "is_there_big_letters":False, "is_there_numbers":False, "is_there_special_charecters":False}
    
    for char in password:
        ascii_value = ord(char)
        if 97 <= ascii_value and ascii_value <= 122:
            bool_dict["is_there_small_letters"] = True
        elif 65 <= ascii_value and ascii_value <= 90:
            bool_dict["is_there_big_letters"] = True
        elif 48 <= ascii_value and ascii_value <= 57:
            bool_dict["is_there_numbers"] = True
        elif (33 <= ascii_value and ascii_value <= 47) or (58 <= ascii_value and ascii_value <= 64) or (91 <= ascii_value and ascii_value <= 96) or (123 <= ascii_value and ascii_value <= 126):
            bool_dict["is_there_special_charecters"] = True
    
    points = 0
    for value in bool_dict.values():
        if value == True:
            points += 1
    return points

def PopularWordsCheck():
    global password
    print(f"my password is {password} from PopularWordsCheck")
    if "123" in password:
        return -2
    elif "admin" in password:
        return -2
    else:
        return 0


password = InputPassword()
final_points = LengthCheck() + ComplexityCheck() + PopularWordsCheck()
print(final_points)