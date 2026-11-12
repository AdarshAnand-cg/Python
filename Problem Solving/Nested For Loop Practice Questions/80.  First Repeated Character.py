str=input("Enter The String:-")
for i in range(len(str)):
    for k in range(i):
        if str[i] == str[k]:
            print(str[i])
            break
    else:
        continue

    break
        

