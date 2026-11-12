students = int(input("Enter Students: "))
subjects = int(input("Enter Subjects: "))

for i in range(students):
    total = 0
    highest = -1
    lowest = 101

    for j in range(subjects):
        marks = int(input("Enter Marks: "))
        total += marks

        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks

    print("Student", i+1)
    print("Total =", total)
    print("Average =", total/subjects)
    print("Highest Marks =", highest)
    print("Lowest Marks =", lowest)
