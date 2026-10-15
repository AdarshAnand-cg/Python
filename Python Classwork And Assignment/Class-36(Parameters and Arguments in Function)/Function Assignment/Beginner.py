# Question-1
def welcome():
    print("Wlcome To Python")
welcome()

# Question-2
def greet(name):
    print("Hello!",name)
greet("Adarsh")

# Question-3
def show_number(number):
    print("Selected Number:",number)
show_number(24)

# Question-4
def add(a,b):
    return f"The Sum of these Two numbers :{a+b}"
sum=add(12,87)
print(sum)

# Question-5
def square(number):
    return f"The Square of {number} is {number**2}"
Sq=square(13)
print(Sq)

# Question-6
def is_even(number):
    if number%2==0:
       return True
    else:
        return False
status=is_even(27)
print(status)
   
# Question-7
def get_full_name(first_name,last_name):
    return f"My name is {first_name+last_name}"
full_name=get_full_name("Adarsh"," Anand")
print(full_name)

# Question-8
def introduction(name,city="Pune"):
    return f"My Name is {name}.I live in {city}"
intro=introduction("Rahul Nagar","Mumbai")  #in that case parameter's is replaced by argument
Intro=introduction("Ashish Anand")  
print(f"{intro}\n{Intro}")

# Question-9
def subtract(a,b):
    print(f"The Subtraction of {b} from {a} is {a-b}")
subtract(16,7)

# Question-10
def get_min_max(a,b):
    if a>b:
        return f"The Smaller And Larger Values Are {b} and {a} respectively."
    else:
        return f"The Smaller And Larger Values are {a} and {b} respectively."
numbers=get_min_max(165,98)
print(numbers)