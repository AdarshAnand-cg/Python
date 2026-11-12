string = input("Enter Any String: ")

highest = 0
character = ""

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
            highest = count
            character = string[i]

if character != "":
    print("Most Repeated Character:", character)
    print("Frequency:", highest)
