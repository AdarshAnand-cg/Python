n = int(input("How many numbers do you want to enter? "))
for i in range(n):
    num = int(input("Enter a number: "))
    if num < 0:
        break
    print(num, end=" ")