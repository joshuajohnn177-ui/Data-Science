members = {
    "Joshua": "1234",
    "Arun": "5678",
    "Meena": "0000",
    "Kavin": "0101"
}

print("=== Login System ===")
print("1. Login")
print("2. Register\n")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in members:                 
        if members[username] == password:   
            print("Login Successful! Welcome", username + "!")
        else:
            print(" Password Incorrect! Try again.")
    else:
        print(" Username not found! Please register.")

elif choice == "2":
    new_user = input("Choose a username: ")
    
    if new_user in members:
        print(" Username already exists! Try another one.")
    else:
        new_pass = input("Choose a password: ")
        members[new_user] = new_pass
        print(" Registration Successful! You can login now.")

else:
    print(" Invalid choice!")
