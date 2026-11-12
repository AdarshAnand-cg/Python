stores = int(input("Enter Stores: "))
products = int(input("Enter Products: "))

grand_total = 0

for i in range(stores):
    store_total = 0

    for j in range(products):
        quantity = int(input("Enter Product Quantity: "))
        price = int(input("Enter Product Price: "))
        store_total += quantity*price

    grand_total += store_total
    print("Store", i+1, "Stock Value =", store_total)

print("Total Inventory Value =", grand_total)
