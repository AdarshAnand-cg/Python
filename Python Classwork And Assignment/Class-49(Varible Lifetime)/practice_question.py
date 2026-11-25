# Question A: Local and global names
x = 10

def demo():
    x = 20
    print(x)

demo()
print(x)
# Output:-20 and then 10

# Question B: Assignment after reading
# x = 10

# def demo():
#     print(x)
#     x = 20

# demo()
# Output:-UnboundLocalError. Because print statement is above the variable 'x'.

# Question C: Loop runs zero times
# for value in []:
#     print(value)

# print(value)
# Output:-An Error Occurs , basically an Name Error.

# Question D: Mutable global object
data = {"count": 0}

def update():
    data["count"] += 1

update()
print(data)

# Output:- {"count" : 1}

# Question E: Closure remembers state
def outer():
    x = 1
    def inner():
        return x
    return inner

f = outer()
print(f())
# Output:- 1

# Question F: Comprehension variable
x = 9
values = [x for x in range(3)]
print(x)
print(values)
# Output:- 9 then [0,1,2]

# <<<<<<<<<<<<<<<<<====>>>>>>>>>>>>>>>>
# =====================================
#   PRACTICE QUESTIONS
# ======================================
# <<<<<<<<<<<<<<<<<====>>>>>>>>>>>>>>>>
# 
# ___________
# |Beginner |
# |_________|

# Question:-1
def function1():
    city = "Muzaffarpur"
    print(city)
function1()

# Question:-2
school = "Anand Prep Public School"
def function2():
    global school
    print(school)
function2()

# Question:-3
if True:
    variable_3 = "3rd Question of Beginner Level"
print(variable_3)

# Question-4

for i in range(5):
    variable_4 = "Hello World"
print(variable_4)

# Question-5
# Scope is the term that is generally used in programming language,which means that any variable can be accessed in any file at which level whereas variable lifetime means any variable can make bonding with its value for how long.

# ________________
# |______________ |
# | Intermediate| |
# |_____________| |
# |_______________|

# Question-6
value = 100
def test():
    value = 200
    print(value)
test()
print(value)
# Output:-200 then 100

# Question-7
# clicks = 0
# def click():
#   clicks += 1

# Corrected Version:-
clicks = 0
def click():
    global clicks #Adding 'global' keyword can give access of global variabe in local 
    clicks += 1
    print(clicks)
click()

# Question-8
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

# Reason to raise an error:-Here in the show named function ,print function is written above the name variable which is already printed before assigning also it doesn't access the global varible because, after checking the variable in the function, it actually finds it but can't get the value of the variable as its assigning is after the print statement.
 
# Question-9
def function9_1():
    hello_world = "Hello World"
    def function9_2():
        print(hello_world)
    function9_2()
function9_1()

# Question-10
def function10():
    list_10 = ["I", "Am", "Atomic"]
    return list_10
print(function10())

# _________________________
#|  _____________________  |
#| |  _________________  | |
#| | |  __             | | |
#| | | |__Challenging__| | |
#| | |___________________| |
#| |_______________________|

# Question-11
def function11_1():
    count = 0
    def function11_2():
        nonlocal count
        count += 1
        print(count)
    return function11_2
counter = function11_1()
counter()  # 1
counter()  # 2
counter()  # 3

# Question-12
x = 1
def outer():
    x = 2
    def inner():
        x = 3
        print(x)
    inner()
    print(x)
outer()
print(x)
# Output:- 3 ,then 2 and then 1

# Question-13
# Ans:- This happens because Python treats variables normal in for loops and list comprehensions differently in terms of scope.

# Question-14
def make_counter():
    count = 0
    def increment():
        nonlocal count  
        count += 1
        return count
    return increment
new_variable = make_counter()
print(new_variable())
print(new_variable())
print(new_variable())

# Question-15
# Ans:-because the words like 'list','str' and 'sum' because they are used in python for some built in keywords









