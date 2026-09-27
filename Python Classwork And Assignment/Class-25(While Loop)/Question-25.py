text = input("Enter a string: ")

i = 0
count = 0

while i < len(text):
    if text[i].isupper():
        count += 1
    i += 1

print("Number of uppercase letters:", count)