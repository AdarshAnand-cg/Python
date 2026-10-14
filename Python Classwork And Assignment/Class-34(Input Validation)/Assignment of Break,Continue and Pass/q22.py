num=[12,34,32,15,51,51,18,12,5,15,59,55,75,19,14,55,4,54,4,1,5,48,51,84,2,51,21,61,1,50,62,55,5,53,5]
target=int(input("Enter A Number:-"))
for ch in num:
    if target==ch:
        print("Found")
        break
else:
    print("Not-Found")