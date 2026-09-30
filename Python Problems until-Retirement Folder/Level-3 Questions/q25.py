string=input("Enter The String:-").lower()
i=0
j=len(string)-1
flag=True
while i<j:
    if string[i]==string[j]:
        flag=True
    else:
        flag=False
    i=j
if flag==True:
    print("Palandrome")
else:
    print("This Is not Palandrome")
        