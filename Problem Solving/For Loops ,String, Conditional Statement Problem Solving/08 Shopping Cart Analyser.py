count_budget=0
count_regular=0
count_premium=0
count_luxury=0
total_price=0
for i in range(0,8):
    price=int(input("Enter the Product Prices:-"))
    if price>5000:
        print("Luxury")
        count_luxury+=1
        total_price+=price
    elif price>=2000:
        print("Premium")
        count_premium+=1
        total_price+=price
    elif price>500:
        print("Regular")
        count_regular+=1
        total_price+=price
    else:
        print("Budget")
        count_budget+=1
        total_price+=price

print(f"The Total Price Of All The Amount is {total_price}")
print(f"The Average of All The Amount of Products is {total_price/8}")

print(f"The Number of Product in Budget Section is {count_budget}")
print(f"The Number of Product in Regular Section is {count_regular}")
print(f"The Number of Product in Prremium Section is {count_premium}")
print(f"The Number of Product in Luxury Section is {count_luxury}")

