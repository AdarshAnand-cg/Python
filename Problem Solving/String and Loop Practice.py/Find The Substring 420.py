text = input("Enter The Number:-")
target = "420"
found = False

for i in range(len(text) - len(target) + 1):
    if text[i:i + len(target)] == target:
        found = True
        break

if found:
    print("Caught")
else:
    print("Escaped")