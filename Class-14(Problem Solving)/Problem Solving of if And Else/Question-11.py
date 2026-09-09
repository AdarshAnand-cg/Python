year=int(input("Enter an Year:-"))
if year%400==0 or year%4==0:
    print("Leap Year")
elif year%400!=0:
    print("Not a Leap Year")
elif year%4==0 and year%100!=0:
    print("Leap Year")