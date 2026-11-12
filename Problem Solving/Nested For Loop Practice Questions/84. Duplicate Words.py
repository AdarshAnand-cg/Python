str = input("Enter First Sentence: ").split()
for i in range(len(str)):
    visited = 0
    for k in range(i):
        if str[i] == str[k]:
            visited == 1

    if visited == 0:
        count = 0
        for j in str:
            if str[i] == j:
                count+=1
        if count > 0:
            print("["+str[i], end="] ")
            break