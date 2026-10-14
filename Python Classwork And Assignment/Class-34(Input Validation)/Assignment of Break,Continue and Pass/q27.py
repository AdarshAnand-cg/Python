string=input("Enter Any String:-")
for ch in string:
    if string.count(ch)>=2:
        print(ch)
        break
else:
    print("No Repeated Character")
