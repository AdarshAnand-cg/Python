start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

for num in range(start, end+1):
    temp = num
    digits = 0

    if temp == 0:
        digits = 1

    while temp > 0:
        digits += 1
        temp //= 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        power = 1

        for i in range(digits):
            power *= digit

        total += power
        temp //= 10

    if total == num:
        print(num, end=" ")
