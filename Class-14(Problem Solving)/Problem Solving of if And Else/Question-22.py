Account_balance=int(input("Enter Your Account Balance:Rs "))
Withdrawal_amount=int(input("Enter the amount of money ,you want to withdraw:Rs "))
if Withdrawal_amount>0 and Withdrawal_amount%100==0 and Withdrawal_amount<Account_balance and Account_balance-Withdrawal_amount>=500:
    print("Withdrawl successful")
else:
    print("Withdrawl Unsuccessful")