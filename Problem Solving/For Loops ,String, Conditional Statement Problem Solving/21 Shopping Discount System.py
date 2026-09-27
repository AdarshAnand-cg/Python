price=discount_price=count_discount=0
for i in range(1,11):
    price_variable=int(input("Enter the Product Price:-"))
    if price_variable>=5000:
        count_discount+=1
        price+=price_variable
        print(f"The Price of The product after discount is{price_variable*0.8}")
        discount_price+=price_variable*0.2
    elif price_variable>=3000:
        count_discount+=1
        price+=price_variable
        discount_price+=price_variable*0.15
        print(f"The Price of The product after discount is{price_variable*0.85}")
    elif price_variable>1000:
        count_discount+=1
        price+=price_variable
        discount_price+=price_variable*0.10
        print(f"The Price of The product after discount is{price_variable*0.90}")
    else:
        price+=price-price_variable
        print(f"The Price of The prroduct is {price_variable}")
        discount_price+=0

print(f"The Total Price of products is {price}")
print(f"The Total number of products which gets discount is {count_discount}")
print(f"The Total Discount Price Is {discount_price}")




    
    
