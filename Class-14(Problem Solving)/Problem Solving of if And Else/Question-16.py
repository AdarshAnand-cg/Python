Electricity_Bill=int(input("Enter Your Electricity Bill in units:"))
if Electricity_Bill<=100:
    print(f"The {Electricity_Bill} in Rupees is Rs {Electricity_Bill*5}/-")
elif Electricity_Bill<=200 and Electricity_Bill>100:
    print(f"The {Electricity_Bill} in Rupees is Rs {Electricity_Bill*7}/-")
else:
    print(f"The {Electricity_Bill} in Rupees is Rs {Electricity_Bill*10}/-")