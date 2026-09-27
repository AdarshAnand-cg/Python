string=input("Enter Any String(Print only characters that appear more than once):-")

for ch in string:
    count=0
    for a in string:
        if ch==a:
            count+=1

    if count>1:
        if count == 2:
            print(ch, "=", count, "times -> Duplicate")
        elif count <= 4:
            print(ch, "=", count, "times -> Repeated")
        else:
            print(ch, "=", count, "times -> Highly Repeated")
print() 