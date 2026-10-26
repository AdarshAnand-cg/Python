variable=100
def adarsh():
    # variable+=100
    print(variable)
adarsh()  

# Traceback (most recent call last):
#   File "c:\Users\adars\Desktop\Python\Python-01\Python Classwork And Assignment\Class-43(Variable scope in Function)\classPractice.py", line 5, in <module>
#     adarsh()
#     ~~~~~~^^
#   File "c:\Users\adars\Desktop\Python\Python-01\Python Classwork And Assignment\Class-43(Variable scope in Function)\classPractice.py", line 3, in adarsh
#     variable+=100
#     ^^^^^^^^
# UnboundLocalError: cannot access local variable 'variable' where it is not associated with a value



variable=100
def adarsh():
    var=variable+100
    print(var)
adarsh()  #Output as 200

