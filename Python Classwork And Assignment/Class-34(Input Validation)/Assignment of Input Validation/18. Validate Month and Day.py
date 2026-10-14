month = int(input("Enter month number (1 to 12): "))
while month < 1 or month > 12:
    print("Invalid Month!")
    month = int(input("Enter month number (1 to 12): "))
day = int(input("Enter day number (1 to 31): "))
while day < 1 or day > 31:
    print("Invalid Day!")
    day = int(input("Enter day number (1 to 31): "))
print("Month:", month)
print("Day:", day)