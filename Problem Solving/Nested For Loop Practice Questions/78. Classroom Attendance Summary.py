students = int(input("Enter Students: "))
days = int(input("Enter Days: "))

for i in range(students):
    present = 0
    absent = 0

    for j in range(days):
        attendance = input("Enter P/A: ").upper()

        if attendance == "P":
            present += 1
        else:
            absent += 1
    print("Student", i+1)
    print("Present =", present)
    print("Absent =", absent)

    
