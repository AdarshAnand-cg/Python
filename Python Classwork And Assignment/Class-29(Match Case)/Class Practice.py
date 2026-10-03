
# a=1
# match a:
#     case 1:
#         print("Demo")
#     case _:
#         print("Default Value")


num1=int(input("Enter The First Number:-"))
num2=int(input("Enter The Second Number:-"))
operation=int(input("Enter The Operation's Serial Number You Want TO Perform from Th eollowing:-\n1. Additin\n2. Subtraction\n3. Product\n4. Division\n5. Quit\nEnter Your Response:-"))
while operation!=5:
    match operation:
        case 1:
            print(f"The Addition of {num1} and {num2} is {num1+num2}")
        case 2:
            print(f"The Subtraction of {num2} from {num1} is {num1-num2}")
        case 3:
            print(f"The Product of {num1} and {num2} is {num1*num2}")
        case 4:
            print(f"The Division of {num2} by {num1} is {num1/num2}")
        case _:
            print("Oops!\nInvalid Input.Please Try Again")
    operation=int(input("Enter The Operation's Serial Number You Want TO Perform from Th eollowing:-\n1. Additin\n2. Subtraction\n3. Product\n4. Division\n5. Quit\nEnter Your Response:-"))
print()