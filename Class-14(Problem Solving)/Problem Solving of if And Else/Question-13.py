character=input("Enter any alphabet:-").upper()
if character.isalpha():
    if character=="A" or character=="E" or character=="I" or character=="O" or character=="U" :
        print("Vowel")
    else :
        print("Consonant")
else:
    print("Invalid Input")