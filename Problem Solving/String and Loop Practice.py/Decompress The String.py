sequence=input("Input should be typed as a Eg:-v3k4\nEnter a string containing lowercase English letters followed by integers:-")
letters = ""
num = 0
result = ""

for i in range(len(sequence)):
    if sequence[i].isalpha():
        letters = sequence[i]

    elif sequence[i].isdigit():
        num = int(sequence[i])
        result += letters * num

print(result)
