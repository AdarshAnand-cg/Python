string = input("Enter a string: ")
character = input("Enter a character to remove: ")
for ch in string:
    if ch==character:
        continue
    print(ch, end="")