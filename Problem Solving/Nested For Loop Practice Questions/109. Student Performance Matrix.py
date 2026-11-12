students = int(input("Enter Students: "))
subjects = int(input("Enter Subjects: "))

highest_total = -1
lowest_total = 999999
top_student = 0
low_student = 0

for i in range(students):
    total = 0
    passed = 1

    for j in range(subjects):
        marks = int(input("Enter Marks: "))
        total += marks

        if marks < 40:
            passed = 0

    average = total/subjects
    print("Student", i+1, "Total =", total, "Average =", average)

    if passed == 1:
        print("Result: Pass")
    else:
        print("Result: Fail")

    if total > highest_total:
        highest_total = total
        top_student = i+1

    if total < lowest_total:
        lowest_total = total
        low_student = i+1

print("Highest Student =", top_student, "Total =", highest_total)
print("Lowest Student =", low_student, "Total =", lowest_total)
