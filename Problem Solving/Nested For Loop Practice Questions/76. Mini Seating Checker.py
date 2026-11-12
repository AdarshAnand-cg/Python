rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))

for i in range(rows):
    for j in range(1, columns+1):
        print(chr(65+i) + str(j), end=" ")

    print()