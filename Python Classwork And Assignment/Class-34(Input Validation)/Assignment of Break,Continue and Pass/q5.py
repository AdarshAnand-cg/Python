word = input("Enter a string: ")
target = input("Enter the target character: ")
for ch in word:
    print(ch, end=" ")
    if ch == target:
        break

