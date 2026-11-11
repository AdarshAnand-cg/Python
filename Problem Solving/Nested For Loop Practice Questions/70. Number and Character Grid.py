alphabet=input("Enter the word:-")
n=int(input("Enter N:-"))
for i in alphabet:
    for j in range(1,n+1):
        print(f"{i}{j} ",end="")
    print()