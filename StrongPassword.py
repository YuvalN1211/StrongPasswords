def InputPassword():
    password = str(input("Enter your password: "))
    if(len(password) == 0):
        InputPassword()
    else:
        return password

def LengthCheck(password, CurrentPoints):
    if len(password) < 8:
        return CurrentPoints
    elif len(password) < 12:
        return CurrentPoints + 1
    else:
        return CurrentPoints + 2

