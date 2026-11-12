string = input("Enter Any String: ")

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

        print(string[i], ":", end=" ")
        for j in range(count):
            print("*", end="")
        print(count)
