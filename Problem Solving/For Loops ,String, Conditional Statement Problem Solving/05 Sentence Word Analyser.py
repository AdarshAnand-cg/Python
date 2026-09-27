short_word=0
medium_word=0
long_word=0
sentence=input("Enter Any Sentence:-")
word=sentence.split()

for ch in word:
    if len(ch)<=3 and len(ch)>=0:
        print("Short")
        short_word+=1
    elif len(ch)>4 and len(ch)<=6:
        print("Medium")
        medium_word+=1
    elif len(ch)>6:
        print("Long")

print(f"The Number Of Short Words is {short_word}")
print(f"The Number Of medium Words is {medium_word}")
print(f"The Number Of long Words is {long_word}")