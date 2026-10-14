n=int(input("Enter any Number:-"))
count=0
for i in range(2,n-1):
    if n%i==0:
        count+=1
if count==0:
    print(f"`{n}` `Prime`")
else:
    print(f"`{n}` `Not a Prime`")