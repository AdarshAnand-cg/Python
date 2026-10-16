sentence=input("Enter Any Sentence:-").split()
target_word="Adarsh"
while True:
    if target_word in sentence:
        print("Found")
        break
    else:
        print("Not Found")
    sentence=input("Enter Any Sentence:-").split()
    



