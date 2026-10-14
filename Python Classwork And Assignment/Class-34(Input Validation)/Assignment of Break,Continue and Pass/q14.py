marks=input("Enter Your Marks:-")
i=marks.split()
for ch in i:
    if int(ch)<40 or int(ch)>100:
        continue
    print(ch,end=" ")


