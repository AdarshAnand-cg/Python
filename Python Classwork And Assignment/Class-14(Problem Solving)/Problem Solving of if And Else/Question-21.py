a=int(input("Enter the First side of Triangle:"))
b=int(input("Enter the second side of Triangle:"))
c=int(input("Enter the Third side of Triangle:"))
if a+b>c and b+c>a and a+c>b:
    print ("These Three sides can make Triangle")
    if a==b==c:
        print("This Triangle is Equilateral Triangle")
    elif a==b or a==c or b==c:
        print("This Triangle is Isoceles Triangle")
    else :
        print("This Triangle is Scalene Triangle")
else:
    print("These Three sides can't Make a triangle")
    