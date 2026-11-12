n = int(input("Enter Matrix Size: "))
matrix = [0] * (n * n)

for i in range(n):
    for j in range(n):
        matrix[i*n+j] = int(input("Enter Value: "))

total = 0
border = 0
main_diagonal = 0
opposite_diagonal = 0
inner = 0

for i in range(n):
    for j in range(n):
        value = matrix[i*n+j]
        total += value

        if i == 0 or j == 0 or i == n-1 or j == n-1:
            border += value
        else:
            inner += value

        if i == j:
            main_diagonal += value

        if i + j == n-1:
            opposite_diagonal += value

print("Total =", total)
print("Border Total =", border)
print("Main Diagonal =", main_diagonal)
print("Opposite Diagonal =", opposite_diagonal)
print("Inner Total =", inner)
