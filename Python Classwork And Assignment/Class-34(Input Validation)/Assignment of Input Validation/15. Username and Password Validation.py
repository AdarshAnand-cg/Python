username = input("Enter username: ")
password = input("Enter password: ")
while (len(username.strip()) < 5 or " " in username.strip() or len(password) < 8 or password.strip() == ""):
    print("Invalid Username or Password!")
    username = input("Enter username: ")
    password = input("Enter password: ")
print("Username and Password are valid!")
print("Registration Successful!")