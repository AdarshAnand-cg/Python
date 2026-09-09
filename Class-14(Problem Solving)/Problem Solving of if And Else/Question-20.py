print("For Checking Whether Three sides can Make a triangle or not.Click Enter and Give the Sides Value as Follows:")
a=int(input("Enter the First side of Triangle:"))
b=int(input("Enter the second side of Triangle:"))
c=int(input("Enter the Third side of Triangle:"))
if a+b>c and b+c>a and a+c>b:
    print ("These Three sides can make Triangle")
else:
    print("These Three sides can't Make a triangle")
