even = 0
odd = 0
positive = 0
negative = 0
zero = 0
largest = 0

matrix= ""   # will store the matrix to print at the end

print("Enter 9 numbers for the 3 x 3 matrix:")

for i in range(3):
    row = ""   # stores one row as text

    for j in range(3):
        num = int(input("Enter number: "))

        # Add this number to the current row
        row = row + str(num) + "   "

        # Check even or odd
        if num % 2 == 0:
            even = even + 1
            print(num, "is Even")
        else:
            odd = odd + 1
            print(num, "is Odd")

        # Check positive, negative or zero
        if num > 0:
            positive = positive + 1
            print(num, "is Positive")
        elif num < 0:
            negative = negative + 1
            print(num, "is Negative")
        else:
            zero = zero + 1
            print(num, "is Zero")

        # Find the largest number
        if i == 0 and j == 0:
            largest = num
        elif num > largest:
            largest = num

    # After each row is finished, add it to the matrix text
    matrix = matrix + row + "\n"

print()
print("The 3 x 3 Matrix is:")
print(matrix)

print("Even count:", even)
print("Odd count:", odd)
print("Positive count:", positive)
print("Negative count:", negative)
print("Zero count:", zero)
print("Largest number:", largest)