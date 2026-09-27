maths_marks=int(input("Enter Your Marks in Mathematics: "))
physics_marks=int(input("Enter Your Marks in Phyics: "))
chemistry_marks=int(input("Enter Your Marks in Chemistry: "))

if maths_marks>0 and maths_marks<100:
    if maths_marks>=75:
        print("Distinction")
    elif maths_marks>=60:
        print("First Class")
    elif maths_marks>=50:
        print("Second Class")
    else :
        print("Pass")
else:
    print("Fail")

if physics_marks>0 and physics_marks<100:
    if physics_marks>=75:
        print("Distinction")
    elif physics_marks>=60:
        print("First Class")
    elif physics_marks>=50:
        print("Second Class")
    else :
        print("Pass")
else:
    print("Fail")

if chemistry_marks>0 and chemistry_marks<100:
    if chemistry_marks>=75:
        print("Distinction")
    elif chemistry_marks>=60:
        print("First Class")
    elif chemistry_marks>=50:
        print("Second Class")
    else :
        print("Pass")
else:
    print("Fail")
