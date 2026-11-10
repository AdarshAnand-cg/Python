sentence = input("Enter Sentence:-").split()

for i in range(len(sentence)):
    for j in range(len(sentence)):
        difference = len(sentence[i]) - len(sentence[j])

        if difference < 0:
            difference = -difference

        print(f"{sentence[i]}-{sentence[j]} = {difference}")