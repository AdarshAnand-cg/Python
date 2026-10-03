# row = 0
# while row<=6:
#     column=0
#     while column<=row:
#         column+=1
#         if column==1 or column==3 or column==5 or column==7:
#             print(column,end=" ")
#         else:
#             print("*",end=" ")
#     print()
#     row+=1






# string=input("Enter Any String:-")
# final=""
# for ch in string:
#     if ch.isalpha():
#         final+=ch
# print(final)

# input=input("Enter Any String:-")
# lower=""
# count=0
# for i in input:
#     if i.islower():
#         count+=1
#         lower=i
#         print(lower,end=",")
# print(f"\nThe Total Number of Lowercase is {count}")



a=input("Enter Any String")
b=""
c=0
for i in a:
    if i.isalpha():
        b+=i
    elif i.isdigit():
        c+=int(i)
    else:
        b="Special Characters"
print(b,end="")
print(f"\n{c}")