n = int(input("Enter N: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        value = i*j

        if value % 15 == 0:
            print("FizzBuzz", end=" ")
        elif value % 3 == 0:
            print("Fizz", end=" ")
        elif value % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(value, end=" ")

    print()
