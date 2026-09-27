total_revenue = 0

for i in range(1, 7):
    units = int(input("Enter units used by customer " + str(i) + ": "))

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    elif units <= 400:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    else:
        bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 15)

    if bill < 1000:
        category = "Low"

    elif bill <= 3000:
        category = "Medium"

    else:
        category = "High"

    print("Customer", i, "Bill =", bill)
    print("Category =", category)

    total_revenue += bill

print("Total Revenue =", total_revenue)