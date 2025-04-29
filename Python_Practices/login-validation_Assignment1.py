print("GTST COMPANY LOGIN PAGE")

users = {'Nathan':'2313', 'Geez':'pass231', 'Abebe':'092313133', 'Miki':"pl3s34D0n'tH4ckM3"}
i = 1
x = 5
while i <= 5:
    username = input("Enter Username: ")
    password = input("Enter password: ")
    i = i+1
    x = x-1
    try:
        if users[username] == password:
            print("Login successful!!\n Welcome to GTST company!!")
            break
        else:
            print("Incorrect login!") 
            if i <= 5:
                print(f"Try again, you can try {x} times!")
            elif i >= 5:
                print("Sorry you are limited!!")
                break  
    except KeyError:
        print("Incorrect login!") 
        if i <= 5:
            print(f"Try again, you can try {x} times!")
        else:
            print("Sorry you are limited!!")
            break  
    