# # variable=100
# # def adarsh():
# #     # variable+=100
# #     print(variable)
# # adarsh()  

# # # Traceback (most recent call last):
# # #   File "c:\Users\adars\Desktop\Python\Python-01\Python Classwork And Assignment\Class-43(Variable scope in Function)\classPractice.py", line 5, in <module>
# # #     adarsh()
# # #     ~~~~~~^^
# # #   File "c:\Users\adars\Desktop\Python\Python-01\Python Classwork And Assignment\Class-43(Variable scope in Function)\classPractice.py", line 3, in adarsh
# # #     variable+=100
# # #     ^^^^^^^^
# # # UnboundLocalError: cannot access local variable 'variable' where it is not associated with a value



# # variable=100
# # def adarsh():
# #     var=variable+100
# #     print(var)
# # adarsh()  #Output as 200
# def check(x):
#     if x > 10:
#         return x * 2

#     return x + 2

# print(check(8))
# print(check(15))
# x = 0

# for i in range(1, 5):
#     x += i

#     if x > 5:
#         break

# print(x)

# for i in range(1, 4):
#     for j in range(i):
#         print(j, end="")
#     print()

x = "global"
def outer():
    x = "enclosing"
    def inner():
        return x
    return inner()

print(outer())