character=input("Enter The Character:-")
print(f"The Pairs Whose ASCII Differnce is More Than 6 is as:-")
for i in range(len(character)):
    for j in range(i+1,len(character)):
        difference=ord(character[i])-ord(character[j])
        if difference<0:
            difference=difference*-1
        if difference>=6:
            print("("+character[i]+"-"+character[j]+")",end=" ")

