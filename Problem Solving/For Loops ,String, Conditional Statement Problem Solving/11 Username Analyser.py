first_Character=""
count_underscore=0
count_digit=0
for i in range(0,5):
    username=input("Enter Your Username:-")
    for ch in username:
        for a in ch:
            if a=="_":
                count_underscore+=1
            elif a.isdigit():
                count_digit+=1
    length=len(username)
    first_Character=username[0:1]
    print(f"The first character of the usernamse is {first_Character}")
    print(f"The Length of The Username is {length}")

print(f"The Total Number of Underscore in Username is {count_underscore}")
print(f"The Total Number Of Digits is {count_digit}")


