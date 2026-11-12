str1 = input("Enter First Sentence: ").split()
str2 = input("Enter Second Sentence: ").split()
for i in range(len(str1)):
    visited = 0

    for k in range(i):
        if str1[i] == str1[k]:
            visited = 1

    if visited == 0:
        for j in str2:
            if str1[i] == j:
                print("["+str1[i], end="] ")
                break