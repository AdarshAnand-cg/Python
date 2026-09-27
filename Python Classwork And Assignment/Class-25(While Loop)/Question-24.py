n=input("Enter Any String:").upper()
i=0
count=0
while i<len(n):
    if i=="a":
        count+=1
    else:
        count+=0
    i+=1
print(count)
