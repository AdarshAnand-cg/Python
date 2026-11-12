customers = int(input("Enter Customers: "))
products = int(input("Enter Products: "))

grand_total = 0

for i in range(customers):
    total = 0

    for j in range(products):
        price = int(input("Enter Product Price: "))
        total += price

    grand_total += total
    print("Customer", i+1, "Total =", total)

print("Grand Total =", grand_total)
