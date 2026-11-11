sentence = input("Enter Sentence:-").split()

for i in range(len(sentence)):
    for j in range(i+1, len(sentence)):
        if sentence[i][0] == sentence[j][0]:
            result = "Same"
        else:
            result = "Different"

        print(f"{sentence[i]} ({len(sentence[i])}) - {sentence[j]} ({len(sentence[j])}) = {result}")