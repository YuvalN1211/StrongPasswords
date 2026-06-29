password = str(input("Enter yuor password: "))


def LengthCheck(password, CurrentPoints):
    if len(password) < 8:
        return CurrentPoints
    elif len(password) < 12:
        return CurrentPoints + 1
    else:
        return CurrentPoints + 2











if __name__ == "__main__":
    print("Im main :)")