Electricity_Bill=int(input("Enter Your Electricity Bill in units:"))
if Electricity_Bill<=100:
    print(f"The Electricity Bill in Rupees is Rs {Electricity_Bill*5}/-")
elif Electricity_Bill>100 and Electricity_Bill<=200:
    print(f"The Electricity Bill in Rupees is Rs {(Electricity_Bill-100)*7+(100*5)}/-")
else:
    print(f"The Electricity Bill in Rupees is Rs {(Electricity_Bill-200)*10+(100*7)+(100*5)}/-")