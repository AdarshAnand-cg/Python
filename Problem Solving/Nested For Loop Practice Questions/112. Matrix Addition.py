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

print("Addition")
for i in range(rows):
    for j in range(columns):
        print(matrix1[i*columns+j] + matrix2[i*columns+j], end=" ")
    print()
