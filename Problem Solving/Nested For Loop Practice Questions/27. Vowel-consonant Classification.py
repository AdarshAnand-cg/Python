string=input("Enter Any String:-")
for i in string:
    if i in "AEIOUaeiou":
        print(f"{i} = Vowel")
    else:
        print(f"{i} = Consonant")