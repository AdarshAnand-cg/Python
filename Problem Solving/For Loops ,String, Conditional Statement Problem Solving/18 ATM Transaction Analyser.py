balance=1000
count=0
for i in range(1,8):
    count+=1
    confirmation=int(input("Choose The Following Options for Transaction(Either '1' or '2'):\n1.Deposit\n2.Withdrawl\nEnter Your Response:-"))
    if confirmation==1:
        money_deposit=int(input("Enter The Amount Of Money You Want to Deposit:-₹"))
        balance+=money_deposit
    elif confirmation==2:
        money_withdrawl=int(input("Enter The Amount Of Money You Want to Withdraw:-₹"))
        balance-=money_withdrawl
        if money_withdrawl>balance:
                print("Balance is insufficient")
        else:
            continue
    else:
        print("Invalid Input")
    if balance<1000:
        print("Low Balance")
    

print(f"The final Balance is ₹{balance}")
print(f"The total Transaction counts as {count}")
    
    