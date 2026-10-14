password = input("Enter your password: ")
while len(password) < 8 or password.islower() or password.isupper() or password.isalpha() or " " in password:
    print("Password does not meet the following rules:")
    if len(password) < 8:
        print("Password must contain at least 8 characters.")
    upper=lower=digit=space=False
    for ch in password:
        if ch >= "A" and ch <= "Z":
            upper = True
        if ch >= "a" and ch <= "z":
            lower = True
        if ch >= "0" and ch <= "9":
            digit = True
        if ch == " ":
            space = True
    if upper == False:
        print("Password must contain at least one uppercase letter.")
    if lower == False:
        print("Password must contain at least one lowercase letter.")
    if digit == False:
        print("Password must contain at least one digit.")
    if space == True:
        print("Password must not contain whitespace.")
    password = input("Enter your password again: ")
print("Password accepted!")