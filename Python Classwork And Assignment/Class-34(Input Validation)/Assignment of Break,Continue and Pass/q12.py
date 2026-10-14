n=int(input("Enter Any Integer:-"))
for i in range(1,n+1):
    if i%3==0:
        continue
    else:
        print(i)
    i+=1

