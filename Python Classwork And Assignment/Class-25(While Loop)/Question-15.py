n=int(input("Enter Any Number:-"))
count=0
i=2
while i<=n:
    if i%2==0:
        count+=1
    else :
        count+=0
    i+=1
print(f"The Number of Even Numbers Before {n} is {count}")