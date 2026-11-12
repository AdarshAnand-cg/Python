rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))

matrix1 = [0] * (rows * columns)
matrix2 = [0] * (rows * columns)

print("Enter First Matrix")
for i in range(rows):
    for j in range(columns):
        matrix1[i*columns+j] = int(input("Enter Value: "))

print("Enter Second Matrix")
for i in range(rows):
    for j in range(columns):
        matrix2[i*columns+j] = int(input("Enter Value: "))

same = 0
different = 0

for i in range(rows):
    for j in range(columns):
        if matrix1[i*columns+j] == matrix2[i*columns+j]:
            same += 1
        else:
            different += 1

print("Same Positions =", same)
print("Different Positions =", different)
