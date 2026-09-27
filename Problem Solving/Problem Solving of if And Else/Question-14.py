cost_price=int(input("Enter the Cost Price:Rs/-"))
selling_price=int(input("Enter the Selling Price:Rs/-"))

if cost_price>selling_price:
    print(f"Loss is :Rs/-{cost_price-selling_price}")
elif selling_price>cost_price:
    print(f"Profit is :Rs/-{selling_price-cost_price}")
else :
    print("No profit and no loss")