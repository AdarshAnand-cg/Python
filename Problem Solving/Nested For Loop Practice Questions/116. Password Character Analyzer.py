password = input("Enter Password: ")

upper = 0
lower = 0
digits = 0
special = 0

for i in password:
    if "A" <= i <= "Z":
        upper += 1
    elif "a" <= i <= "z":
        lower += 1
    elif "0" <= i <= "9":
        digits += 1
    else:
        special += 1

print("Uppercase =", upper)
print("Lowercase =", lower)
print("Digits =", digits)
print("Special Characters =", special)
