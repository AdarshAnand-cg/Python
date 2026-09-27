for i in range(5):
    password = input("Enter password: ")

    length = False
    uppercase = False
    lowercase = False
    digit = False
    special = False

    if len(password) >= 8:
        length = True

    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            uppercase = True
        elif ch >= 'a' and ch <= 'z':
            lowercase = True
        elif ch >= '0' and ch <= '9':
            digit = True
        else:
            special = True

    count = 0

    if length:
        count += 1
    if uppercase:
        count += 1
    if lowercase:
        count += 1
    if digit:
        count += 1
    if special:
        count += 1

    if count == 5:
        print("Strong")
    elif count >= 3:
        print("Medium")
    else:
        print("Weak")