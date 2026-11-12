numbers = input("Enter Numbers: ").split()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        count = 0

        for k in range(len(numbers[i])):
            visited = 0

            for x in range(k):
                if numbers[i][k] == numbers[i][x]:
                    visited = 1

            if visited == 0:
                for y in numbers[j]:
                    if numbers[i][k] == y:
                        count += 1
                        break

        print(numbers[i], numbers[j], "Common Digits =", count)
