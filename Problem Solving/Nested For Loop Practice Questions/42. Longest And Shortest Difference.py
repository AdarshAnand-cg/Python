sentence = input("Enter Sentence:-").split()

longest = sentence[0]
shortest = sentence[0]

for i in sentence:
    for j in sentence:
        if len(i) > len(longest):
            longest = i

        if len(j) < len(shortest):
            shortest = j

print("Longest =", longest)
print("Shortest =", shortest)