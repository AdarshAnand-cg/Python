# str=input("Enter Any String:-").lower().strip()
# condition=True
# count=0
# all=0
# for i in str:
#     all+=1
#     if i=="o":
#         condition=True
#         count+=1
#         if count==1:
#                 print("'o' is Found in the String At its position in String is/are as follows:")
#         position=count
#         if all==1:
#             print(f"'o' is at {all}st Position in the String.")
#         elif all==2:
#             print(f"'o' is at {all}nd Position in the String.")
#         elif all==3:
#             print(f"'o' is at {all}rd Position in the String.")
#         else :
#             print(f"'o' is at {all}th Position in the String.")
# if condition==True:
#     print(f"The Total Number Of 'o' in String is {count}")


# for i in range(1,10):
#     if i==6:
#         break
#     print(i)

numbers = [10, 20, 30, 40, 50]
for i in numbers:
    if i==30:
        break
    print(i)
print(f"{i}=>Found")

for j in range(1,100):
    if j%17==0:
        break
    print(j)


for e in range(1,20):
    if e%2==0:
        continue
    print(e)

numbers = [10, -2, 30, -5, 40, -8]
for i in numbers:
    if i<0:
        continue
    print(i)

for j in range(1,20):
    if j%3==0:
        continue
    print(j)

numbers = [5, 12, 8, 21, 30, 7]
for i in numbers:
    if i<10:
        continue
    print(i)


input=int(input("Enter Any Number:-"))
if input>0:
    