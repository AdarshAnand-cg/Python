houses = int(input("Enter Houses: "))
months = int(input("Enter Months: "))

highest = -1
highest_month = 0

for i in range(months):
    month_total = 0

    for j in range(houses):
        units = int(input("Enter Units Used by House: "))
        month_total += units

    print("Month", i+1, "Total Usage =", month_total)

    if month_total > highest:
        highest = month_total
        highest_month = i+1

print("Highest Usage Month =", highest_month)
print("Usage =", highest)
