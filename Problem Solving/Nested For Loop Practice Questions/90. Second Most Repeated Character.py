string = input("Enter Any String: ")

highest = 0
second = 0

for i in range(len(string)):
    visited = 0

    for k in range(i):
        if string[i] == string[k]:
            visited = 1

    if visited == 0:
        count = 0
        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1

        if count > highest:
            second = highest
            highest = count
        elif count < highest and count > second:
            second = count

if second == 0:
    print("Second Highest Frequency Not Found")
else:
    print("Second Highest Frequency:", second)
    for i in range(len(string)):
        visited = 0
        for k in range(i):
            if string[i] == string[k]:
                visited = 1
        if visited == 0:
            count = 0
            for j in range(len(string)):
                if string[i] == string[j]:
                    count += 1
            if count == second:
                print(string[i], end=" ")
