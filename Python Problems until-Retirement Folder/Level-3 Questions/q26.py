n=int(input("Enter The Number:-"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("It Is Prime")
else:
    print("It Is Not A Prime Number")
