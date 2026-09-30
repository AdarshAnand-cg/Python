marks = int(input("Enter your marks: "))

if marks>=0 and marks <= 59:
    print("F")
elif marks>=60 and marks<= 69:
    print("D")
elif marks>=70 and marks<= 79:
    print("C")
elif marks>=80 and marks<=89:
    print("B")        
elif marks>=90 and marks<=100:
    print("A")
else:
    print("Enter a valid number")