rows = int(input("Enter Rows: "))
seats = int(input("Enter Seats Per Row: "))

available = 0
booked = 0

for i in range(rows):
    row_available = 0

    for j in range(seats):
        status = input("Enter A for Available and B for Booked: ").upper()

        if status == "A":
            available += 1
            row_available += 1
        else:
            booked += 1

    print("Row", i+1, "Available =", row_available)

print("Total Available =", available)
print("Total Booked =", booked)
