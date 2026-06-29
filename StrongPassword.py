def InputPassword():
    password = str(input("Enter your password: "))
    if(len(password) == 0):
        InputPassword()
    else:
        return password

def LengthCheck(password, current_points):
    if len(password) < 8:
        return current_points
    elif len(password) < 12:
        return current_points + 1
    else:
        return current_points + 2

def ComplexityCheck(password, current_points)
    pass