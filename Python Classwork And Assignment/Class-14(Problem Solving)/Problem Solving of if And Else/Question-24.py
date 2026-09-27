amount=int(input("Enter The Purchase Amount"))

if amount<500:
    discount1=0
    Discount_amount=(amount*discount1)/100
    print(f"Discount Amount:{Discount_amount}\nFinal Amount:Rs{amount-Discount_amount}/-")
elif amount>500 and amount<1000:
    discount2=5
    Discount_amount=(amount*discount2)/100
    print(f"Discount Amount:{Discount_amount}\nFinal Amount:Rs{amount-Discount_amount}/- ")
elif amount>=1000 and amount<2000:
    discount3=10
    Discount_amount=(amount*discount3)/100
    print(f"Discount Amount:{Discount_amount}\nFinal Amount:Rs{amount-Discount_amount}/- ")
elif amount>=2000 and amount<5000:
    discount4=15
    Discount_amount=(amount*discount4)/100
    print(f"Discount Amount:{Discount_amount}\nFinal Amount:Rs{amount-Discount_amount}/- ")
else :
    discount5=20
    Discount_amount=(amount*discount5)/100
    print(f"Discount Amount:{Discount_amount}\nFinal Amount:Rs{amount-Discount_amount}/- ")