while True:
    user = input("Enter username: ")
    pwd = input("Enter Password: ")

    if pwd == 'password1234' and user == 'bob':
        print("Access Granted!!")
        break
    if pwd == 'happyPass122' and user == 'fred':
        print("Access Granted!!")
        break
    if pwd == 'passwithlock44' and user == 'lock':
        print("Access Granted!!")
        break
    else:
        print("Access Denied!")
    
