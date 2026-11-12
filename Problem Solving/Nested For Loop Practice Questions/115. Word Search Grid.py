rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))

grid = [""] * (rows * columns)

for i in range(rows):
    for j in range(columns):
        grid[i*columns+j] = input("Enter Character: ")

target = input("Enter Character to Search: ")
found = 0

for i in range(rows):
    for j in range(columns):
        if grid[i*columns+j] == target:
            print("Found at Row", i+1, "Column", j+1)
            found += 1

if found == 0:
    print("Character Not Found")
else:
    print("Total Occurrences =", found)
