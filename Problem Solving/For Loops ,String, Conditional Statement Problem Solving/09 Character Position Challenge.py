string=input("Enter Any String:-")
word=string.split()
count=0

for ch in word:
    for i in ch:
        count+=1
        print(i,end=",")
        if count%2==0:
            print(f"The Position of The Character is Even")
        else:
            print("The Position of The character is Odd")

        if i in "AaEeIiOoUu":
            print ("This Chararcter is Vowel")
        elif i.isalpha():
            print("The Character is Consonant")
        elif i.isdigit():
            print("it is Digit")
        else:
            print("This Is A Special Character")

