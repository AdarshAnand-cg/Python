num1=int(input("Enter the 1st Number"))
num2=int(input("Enter the 2nd Number"))
num3=int(input("Enter The 3rd Number"))
if num1>=num2 and num1>=num3:
    print(f"The Largest Number is {num1}")
elif num2>=num1 and num2>=num3:
    print(f"The Largest Number is {num2}")
else :
    print(f"The Largest Number is {num3}")
