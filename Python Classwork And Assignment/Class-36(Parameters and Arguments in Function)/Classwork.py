bal=30000
def bank():
        
        
        while True:
            money=int(input("1.For Withdraw\n2.For Deposit\n3.For Check Balance\nEnter Your Response:-"))
            match money:
                case 1:
                    a=int(input("Enter Your Amount You Want To Withdraw:-"))
                    def withdraw(a,b):
                        b =balance-a
                        print("Your Entered Amount:-Rs",a)
                        print("Your Balance Amount:-Rs",b)
                        return b
                    balance = withdraw(a,bal)
                
                case 2:
                    a=int(input("Enter Your Amount You Want To Deposit:-"))
                    def deposit(a,balance):
                        balance+=a
                        print("Your Entered Amount:-Rs",a)
                        print("Your Net Amount:-Rs",balance)
                    balance = deposit(a,balance)
                case 3:
                    a=int(input("1.Yes\n2.No\nEnter Your Response:"))
                    if a==1:
                        def deposit(balance):
                                balance
                                print("Your Balance:-Rs",balance)
                        deposit(balance)
                    elif a==2:
                         money=int(input("1.For Withdraw\n2.For Deposit\n3.For Check Balance\n4.Exit\nEnter Your Response:-"))
                case 4:
                    break
                case _:
                    print("Invalid Input")
            
            

bank()
print("Thanks For Visiting Us!")