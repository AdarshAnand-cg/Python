cost_price=int(input("Enter The Cost price:"))
Selling_price=int(input("Enter The Selling Price:"))
if cost_price>Selling_price and cost_price>0 and Selling_price>0:
    print(f"The loss percent :{((cost_price-Selling_price)*100)/cost_price}%")
elif Selling_price>cost_price and cost_price>0 and Selling_price>0:
    print(f"The profit percent :{((Selling_price-cost_price)*100)/cost_price}%")
else :
    print("Oops!!\nPrice can,t be zero or negative.Retry it")