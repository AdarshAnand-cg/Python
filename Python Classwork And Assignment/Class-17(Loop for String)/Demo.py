#
# word=input("Enter Any String:-")
# count=0
# for i in word:
#     count=count+1
# print(f"The no. of Characters in word {word} is '{count}'")
a="*"
# for i in range(9):
#     for j in range(7):
#         print(".",end="")
#     print()

n = int(input("Whats the number you want to enter: "))
for i in range(0,n+1):
    for j in range(i):
        if i<=9:
            print(i ,end="")
        if i>9:
            print(i,end="0")
    print(i)

for a in range(n-1,-1,-1):
    for b in range(a):
        print(a,end="")
    print(a)  