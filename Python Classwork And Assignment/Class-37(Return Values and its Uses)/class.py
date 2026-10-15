def multiply(a,b):
    return a*b
result=multiply(12,37)
print(result)

# Packed/Tuple Format
def calculate(a,b):
    return a+b,a-b,a*b,a/b
operation=calculate(12,4)
print(operation)
# Unpacked Format
def calculate(a,b):
    return a+b,a-b,a*b,a/b
sum,difference,product,division=calculate(12,4)
print(sum,difference,product,division)


def student(name,age,city):
    print("Adarsh",name="Anand",age=21)