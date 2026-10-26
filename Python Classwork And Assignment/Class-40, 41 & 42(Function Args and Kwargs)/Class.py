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

