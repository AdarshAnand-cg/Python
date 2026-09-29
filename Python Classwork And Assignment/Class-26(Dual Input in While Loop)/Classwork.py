# # Dual Input in While Looop
# number=int(input("Enter Any Number:-"))
# total=0
# while number!=0:
#     total+=number
#     number=int(input("Enter Any Number:-"))
# print(f"The Sum of The Numbers is {total}")

# For Palandrome
# Name=(input("Enter a word:")).lower().strip()
# length=len(Name)-1
# sum=""
# number=0
# while length>=0:
#     sum=sum+Name[length]
#     length-=1

# if Name==sum:
#     print("This Word is Palandrome")
# else :
#     print("THis word isn't Palandrome")



string=input("Enter Any Word:-").lower()
i=0
j=len(string)-1
s = True
while i<j:
    if string[i]==string[j]:
        i+=1
        j-=1
    else:
        s=False
        i=j
if s:
    print(f"{string} is Palandrome")
else:
        print(f"{string} is not A Palandrome")

