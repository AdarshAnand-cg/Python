input1 = input("Enter The First String:- ")
input2 = input("Enter The Second String:- ")
print("Common characters include", end=" ")

for i in range(len(input1)):
    visited = 0
    for k in range(i):
        if input1[i] == input1[k]:
            visited = 1
    if visited == 0:
        for j in input2:
            if input1[i] == j:
                print(input1[i], end=" ")
                break