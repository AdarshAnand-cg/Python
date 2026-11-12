string = input("Enter Any String: ")
result = ""

for i in string:
    visited = 0

    for j in result:
        if i == j:
            visited = 1

    if visited == 0:
        result += i

print(result)