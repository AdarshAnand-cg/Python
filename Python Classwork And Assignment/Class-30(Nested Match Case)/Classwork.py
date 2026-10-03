account = "student"
choice = 2

match account:

    case "student":

        match choice:
            case 1:
                print("View Courses")
            case 2:
                print("View Marks")
            case 3:
                print("View Attendance")
            case _:
                print("Invalid Choice")

    case "teacher":

        match choice:
            case 1:
                print("View Students")
            case 2:
                print("Enter Marks")
            case _:
                print("Invalid Choice")

    case _:
        print("Invalid Account Type")




number=int(input("Enter Any Number:-"))
choice=int(input("To check whether the Number is:-\n1.Even\n2.Odd\n3.Prime\nChoose Any Option:-"))

match choice:
    case 1:
        if number%2==0:
            print("Even Number")
        else:
            print("Not An Even Number")
    case 2:
        if number%2!=0:
            print("It is an Odd Number")
        else:
            print("Not An Odd Number")
    case 3:
        count=0
        for i in range(2,number+1):
            if number%i==0:
                count+=1
        if count==1:
            print("Prime Number")
        else:
            print("Not A Prime Number")
    case _:
        print("Invalid Input")