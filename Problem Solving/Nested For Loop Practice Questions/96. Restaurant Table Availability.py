rows = int(input("Enter Number of Rows: "))
columns = int(input("Enter Tables in Each Row: "))

total_available = 0

for i in range(rows):
    row_available = 0

    for j in range(columns):
        status = int(input("Enter 1 for Available and 0 for Occupied: "))

        if status == 1:
            row_available += 1
            total_available += 1

    print("Row", i+1, "Available Tables =", row_available)

print("Total Available Tables =", total_available)
print("Total Occupied Tables =", rows*columns-total_available)
