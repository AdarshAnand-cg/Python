students = int(input("Enter Students: "))
subjects = int(input("Enter Subjects: "))

class_total = 0
highest_student_total = -1
lowest_student_total = 999999
highest_student = 0
lowest_student = 0
pass_count = 0
fail_count = 0

subject_totals = [0] * subjects

for i in range(students):
    total = 0
    highest_marks = -1
    lowest_marks = 101
    passed = 1

    for j in range(subjects):
        marks = int(input("Enter Marks: "))
        total += marks
        subject_totals[j] += marks

        if marks > highest_marks:
            highest_marks = marks
        if marks < lowest_marks:
            lowest_marks = marks
        if marks < 40:
            passed = 0

    average = total / subjects
    class_total += total

    print("Student", i+1)
    print("Total =", total)
    print("Average =", average)
    print("Highest Marks =", highest_marks)
    print("Lowest Marks =", lowest_marks)

    if passed == 1:
        print("Pass")
        pass_count += 1
    else:
        print("Fail")
        fail_count += 1

    if total > highest_student_total:
        highest_student_total = total
        highest_student = i+1

    if total < lowest_student_total:
        lowest_student_total = total
        lowest_student = i+1

print("Subject Analysis")
highest_subject_total = -1
lowest_subject_total = 999999
highest_subject = 0
lowest_subject = 0

for j in range(subjects):
    print("Subject", j+1, "Total =", subject_totals[j])
    print("Subject", j+1, "Average =", subject_totals[j] / students)

    if subject_totals[j] > highest_subject_total:
        highest_subject_total = subject_totals[j]
        highest_subject = j+1

    if subject_totals[j] < lowest_subject_total:
        lowest_subject_total = subject_totals[j]
        lowest_subject = j+1

print("Class Total =", class_total)
print("Class Average =", class_total / (students * subjects))
print("Highest Student =", highest_student)
print("Lowest Student =", lowest_student)
print("Highest Subject =", highest_subject)
print("Lowest Subject =", lowest_subject)
print("Pass Count =", pass_count)
print("Fail Count =", fail_count)
