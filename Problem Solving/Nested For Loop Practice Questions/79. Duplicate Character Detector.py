str=input("Enter The String:-")
for i in range(len(str)):
    visited = 0
    for k in range(i):
        if str[i] == str[k]:
            # print(str[k],end=",")
            visited = 1
    if visited == 0:
        count=0
        for j in range(len(str)):
            if str[i] == str[j]:
                count+=1
        if count > 1:
            print(str[i],end=",")
            

