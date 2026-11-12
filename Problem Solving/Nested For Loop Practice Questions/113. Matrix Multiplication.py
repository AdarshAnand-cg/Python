r1 = int(input("Enter Rows of First Matrix: "))
c1 = int(input("Enter Columns of First Matrix: "))
r2 = int(input("Enter Rows of Second Matrix: "))
c2 = int(input("Enter Columns of Second Matrix: "))

if c1 != r2:
    print("Matrix Multiplication Not Possible")
else:
    a = [0] * (r1 * c1)
    b = [0] * (r2 * c2)

    print("Enter First Matrix")
    for i in range(r1):
        for j in range(c1):
            a[i*c1+j] = int(input("Enter Value: "))

    print("Enter Second Matrix")
    for i in range(r2):
        for j in range(c2):
            b[i*c2+j] = int(input("Enter Value: "))

    print("Product Matrix")
    for i in range(r1):
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += a[i*c1+k] * b[k*c2+j]
            print(total, end=" ")
        print()
