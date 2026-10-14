number=int(input("Enter any integer from 1 to 10:"))
while number>10 or number<0:
    print("Oops!The Selected Integer is Out Of Range\nPlease Try Again")
    number=int(input("Re-enter any integer from 1 to 10:"))
print("Integer is in Range")
