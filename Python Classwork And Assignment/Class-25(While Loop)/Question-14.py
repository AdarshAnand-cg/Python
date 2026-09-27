n=int(input("Enter Any Number:-"))
i=6
print(f"The Numbers by 2 and 3 both before {n} is as follows:")
while i<n+1:
    if i%2==0 and i%3==0:
        print(i)
    i+=1