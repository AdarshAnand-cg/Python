numb=int(input("Enter any Number:-"))
if numb>0 and numb%2==0:
    print("Positive Even")
elif numb>0 and numb%2!=0:
    print("Positive Odd")
elif numb<0 and numb%2==0:
    print("Negative Even")
elif numb<0 and numb%2!=0:
    print("Negative Odd")
else :
    print("Zero")        