num1=int(input("Enter The First Number:-"))
num2=int(input("Enter The Second Number:-"))
operation=int(input("1.Addition(+)\n2.Subtraction\n3.Multiplication\n4.Division\nEnter The Operator Serial Number:- "))
match operation:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)
    case _:
        print("Invalid Input")