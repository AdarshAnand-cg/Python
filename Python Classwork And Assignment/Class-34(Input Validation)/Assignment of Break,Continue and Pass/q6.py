num=input("Enter The Number Sequence:-").split()
for ch in num:
    if int(ch)<0:
        continue
    else:
        print(ch,end=" ")