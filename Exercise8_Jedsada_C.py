usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput == "Jair9un" and passwordInput == "9006":
    print("Hello sir! What do you like to buy")
    print("1. Iphone 12 mini price: 25000 THB")
    print("2. Iphone 12 price: 30000 THB")
    print("3. Iphone 12 pro price: 35000 THB")
    print("4. Iphone 12 pro max price: 40000 THB")
    userSelect = int(input(">>"))
    if userSelect == 1:
        many = int(input("How many : "))
        total = many * 25000
        print("total : ", total)
    elif userSelect == 2:
        many = int(input("How many : "))
        total = many * 30000
        print("total : ", total)
    elif userSelect == 3:
        many = int(input("How many : "))
        total = many * 35000
        print("total : ", total)
    elif userSelect == 4:
        many = int(input("How many : "))
        total = many * 40000
        print("total : ", total)