count = int(input("How many numbers do you want to enter (1-20): "))
while count<1 or count>20:
    print("Invalid Count!")
    count = int(input("Enter count (1-20): "))
total=0
i=1
while i <= count:
    number = int(input("Enter number: "))
    total += number
    i += 1
average = total/count
print("Average:", average)