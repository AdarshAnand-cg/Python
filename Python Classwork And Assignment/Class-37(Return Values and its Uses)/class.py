# def multiply(a,b):
#     return a*b
# result=multiply(12,37)
# print(result)

# # Packed/Tuple Format
# def calculate(a,b):
#     return a+b,a-b,a*b,a/b
# operation=calculate(12,4)
# print(operation)
# # Unpacked Format
# def calculate(a,b):
#     return a+b,a-b,a*b,a/b
# sum,difference,product,division=calculate(12,4)
# print(sum,difference,product,division)


# def student(name,age,city):
#     print("Adarsh",name="Anand",age=21)

count = 100
def hello():
    print(count)

last = [ 10, 20, 30, 40 ]
last = last.append["Hello World"]
def hello1():
    global last
    last = last.append[ None ]
    def hello2():
        nonlocal last
        last = last.append[ "Hello"]
        print(last())
    hello2()
hello1()
    
        