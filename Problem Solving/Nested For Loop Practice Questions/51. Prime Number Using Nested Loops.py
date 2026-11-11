number=int(input("Enter Any Number:-"))
for i in range(2,number):
    count=0
    for j in range(2,i):
        if i%j == 0:
            count+=1
        else:
            pass
    if count == 0:
        print(i,end=" ")

            