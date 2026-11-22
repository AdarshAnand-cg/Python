# def shadow(a,b,/,*args,**kwargs):
#     print(type(args))
#     print(type(kwargs))
#     return args,a*b,a/b,kwargs
    
# print(shadow(729,27,15,454,555,573,q=12,c=143))

# def add(a,b,c):
#     return a+b+c
# number= {'p':10,'q':20 ,'r':30}
# print(add(20,45,30))
# for i in number:
#     print(i)
a={'p' : 1,'q' : 2,'r' : 3}
b={'s' : 4,'t' : 5}
c={**a,**b}
for i in c:
    if i=="s":
        print("Found")
    else:
        pass



def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length: The rectangle's length.
        width: The rectangle's width.

    Returns:
        The area of the rectangle.
    """
    return length * width
print(calculate_area(12,45))
print(calculate_area.__name__)

"""
1st:- / => Before it only positional argument can be written.
2nd:- * => After Which only Keyword AArgument can be written
3rd:- *args =>After Writing it in Parameter Whatever number of argument is written ,It packs all the argument in a tuple
4th:- **kwargs =>convert into dictionary,but only positional argument(for key-value pair)
5th:- * in arguments =>Unpacking any tuple or list
6th:- ** in argument =>Unpacking from dictionary


"""


def hello(a:int,b:bool,c:None) ->int:
    print(a+b+c)

ads = [12,True,None]
bds = {"a":"ada" ,"b":"rsh","c":"Anand"}
hello(*ads)
hello(**bds)