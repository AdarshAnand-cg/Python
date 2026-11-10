string=input("Enter Any String:-")
for i in string:
    for j in string:
        if ord(i)>=ord(j):
            print(f"{i} - {j} = {ord(i)-ord(j)}")
        else:
            print(f"{j} - {i} = {ord(j)-ord(i)}")

