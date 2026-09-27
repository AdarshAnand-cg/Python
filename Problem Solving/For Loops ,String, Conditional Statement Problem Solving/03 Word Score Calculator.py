sentence = input("Enter a sentence: ")

words = sentence.split()

highest_score = 0
highest_word = ""

for word in words:
    score = 0

    for ch in word:
        if ch in "aeiouAEIOU":
            score += 2
        elif ch.isalpha():
            score += 1
        elif ch.isdigit():
            score += 3
        else:
            score += 4

    print(f"{word}={score}")

    if score > highest_score:
        highest_score = score
        highest_word = word

print(f"Word having highest score:{highest_word}" )
print(f"Highest score: {highest_score}")