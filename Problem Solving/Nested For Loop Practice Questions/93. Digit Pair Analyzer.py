number = input("Enter Any Number: ")

for i in range(len(number)):
    for j in range(i+1, len(number)):
        first = int(number[i])
        second = int(number[j])

        if first == second:
            print(first, second, "Equal")
        elif first < second:
            print(first, second, "Increasing")
        else:
            print(first, second, "Decreasing")
