word=input("Enter A word:-").lower()
for ch in word:
    if ch in "aeiou":
        continue
    print(ch,end=",")