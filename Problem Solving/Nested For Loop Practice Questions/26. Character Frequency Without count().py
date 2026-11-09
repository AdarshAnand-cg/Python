string=input("Enter Any String:-")
for i in range(len(string)):
    count=0
    counted=0
    for k in range(i):
        if string[i]==string[k]:
            counted=1
    if counted==0:
        for j in range(len(string)):
            if string[i]==string[j]:
                count+=1
        print(f"{string[i]} = {count}")