sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    vowels = 0
    consonants = 0

    for ch in word:
        if ch.lower() in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    if vowels > consonants:
        result = "Vowel Heavy"
    elif consonants > vowels:
        result = "Consonant Heavy"
    else:
        result = "Balanced"

    print(word, "->", result)