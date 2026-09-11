word = input("Enter Any String:").lower()

count = 0

for character in word:
    if character == "a":
        count = count + 1

print("Count:", count)