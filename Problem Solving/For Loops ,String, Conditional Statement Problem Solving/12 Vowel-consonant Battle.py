count_vowel=0
count_cons=0
sentence=input("Enter any sentence:-")
list=sentence.split()
for words in list:
    for letters in words:
        if letters in "AaEeIiOoUu":
            count_vowel+=1
        elif letters.isalpha():
            count_cons+1
        else:
            print("Not Any Letter")

if count_vowel>count_cons:
    print("Vowels Win")
elif count_vowel<count_cons:
    print("Consonants Win")
elif count_cons==count_vowel:
    print("Draw")
else:
    print("If You Are Getting This.You Are Putting Wrong Input")
            