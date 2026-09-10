n=int(input("Enter any number:-"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print(f"The Sum of The Even Numbers till {n} :-{sum}")