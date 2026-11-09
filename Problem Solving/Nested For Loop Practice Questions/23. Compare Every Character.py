string=input("Enter Any String:-")
n=0
for i in range(len(string)):
    for j in range(len(string)):
        if string[i]==string[j]:
            print(f"{string[i]}/{string[j]} is same")
        else:
            print(f"{string[i]}/{string[j]} is different")

    