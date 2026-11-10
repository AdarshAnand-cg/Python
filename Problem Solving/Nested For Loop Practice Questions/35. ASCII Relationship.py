string=input("Enter Any String:-")
count=0
for i in range(len(string)):
    visited=0
    for k in range(i):
        if string[i] == string[k]:
            visited = 1
    if visited == 0:
        for j in string:
            if ord(string[i])>ord(j):
                print(f"{string[i]}-->{j} Decreasing")
            elif ord(string[i])<ord(j):
                print(f"{string[i]}-->{j} Increasing")
            else:
                print(f"{string[i]}-->{j} Same")
