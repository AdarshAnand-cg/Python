start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

for num1 in range(start, end+1):
    prime1 = 1

    if num1 < 2:
        prime1 = 0
    else:
        for i in range(2, num1):
            if num1 % i == 0:
                prime1 = 0
                break

    if prime1 == 1:
        for num2 in range(num1+1, end+1):
            prime2 = 1

            if num2 < 2:
                prime2 = 0
            else:
                for j in range(2, num2):
                    if num2 % j == 0:
                        prime2 = 0
                        break

            if prime2 == 1:
                total = num1 + num2
                prime_sum = 1

                if total < 2:
                    prime_sum = 0
                else:
                    for k in range(2, total):
                        if total % k == 0:
                            prime_sum = 0
                            break

                if prime_sum == 1:
                    print(num1, num2)
