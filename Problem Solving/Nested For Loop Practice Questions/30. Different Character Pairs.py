string=input("Enter Any String")
for i in range(len(string)):
    for j in range(len(string)):
        if string[i] == string[j]:
            continue
        else:
            print(f"{string[i]} {string[j]}", end=", ")


            