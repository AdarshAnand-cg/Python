quantity = int(input("Enter product quantity: "))
while quantity <= 0:
    print("Quantity must be greater than zero!")
    quantity = int(input("Enter product quantity: "))
price = int(input("Enter unit price: Rs"))
while price <= 0:
    print("Price must be greater than zero!")
    price = int(input("Enter unit price: Rs"))
total = quantity * price
print("Total Cost: Rs", total)