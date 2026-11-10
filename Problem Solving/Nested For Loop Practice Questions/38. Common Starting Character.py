sentence = input("Enter The Sentence:-").split()

for i in range(len(sentence)):
    for j in range(i+1, len(sentence)):
        if sentence[i][0] == sentence[j][0]:
            print(f"{sentence[i]} {sentence[j]}")