count_vowel=count_characters=count_consonant=count_space=0
grade=""
for i in range(1,6):
    name=input("Enter Your Name:-").upper()
    for ch in name:
        if ch in "AEIOU":
            count_vowel+=1
        elif ch.isalpha():
            count_consonant+=1
        elif ch.isspace():
            count_space+=1
        else:
            print("Invalid Input ")
    marks=int(input("Enter Your Marks:-"))
    if marks>90:
        grade="A+"
    elif marks>80:
        grade="A"
    elif marks>75:
        grade="B"
    elif marks>60:
        grade="C"
    elif marks>50:
        grade="D"
    elif marks>35:
        grade="E"
    elif marks>=0:
        grade="You Are Failed"
    else:
        print("Invalid Input")
        grade="For Getting it,type correct Marks"

    print(f"The Number of Character in Your Name is {count_vowel+count_consonant}\nThe Number of Vowel in Your Name is {count_vowel}\nThe Number of Consonant in Your Name is {count_consonant}")
    if count_vowel>count_consonant:
        print("Vowel is More in Your Name")
    elif count_vowel<count_consonant:
        print("Consonant is More in Your Name")
    else:
        print("")
    print("Grade=",grade)
