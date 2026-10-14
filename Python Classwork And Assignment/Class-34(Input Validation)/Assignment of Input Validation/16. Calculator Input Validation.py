num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid Operator!")
    operator = input("Enter operator (+, -, *, /): ")

while operator == "/" and num2 == 0:
    print("Division by zero is not allowed!")
    num2 = float(input("Enter second number again: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2

print("Result:", result)