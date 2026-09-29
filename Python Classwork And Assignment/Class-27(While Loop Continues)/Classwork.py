num=float(input("Enter any Number:"))
while num>0 or num<0:
    if num>0:
        digits=num%10
        print(int(digits))
        num=num//10
    else:
        digits=num%10
        print(int())

print(-1235%10,-1235//10)
print(-124%10,-124//10)