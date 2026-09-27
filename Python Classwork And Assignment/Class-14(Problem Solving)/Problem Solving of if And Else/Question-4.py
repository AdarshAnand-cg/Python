num1=float(input("Enter The 1st Number: "))
num2=float(input("Enter The 2nd Number: "))
num3=float(input("Enter The 3rd Number: "))
if num1<=num2 and num1<=num3:
    print(f"The Smallest Number is {num1}")
elif num2<=num1 and num2<=num3:
    print(f"The Smallest Number is {num2}")
else:
    print(f"The Smallest Number is {num3}")

