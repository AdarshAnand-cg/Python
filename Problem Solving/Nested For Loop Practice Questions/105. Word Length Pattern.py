words = input("Enter Words: ").split()

for i in range(len(words)):
    for j in range(len(words[i])):
        print("*", end="")
    print(" ", len(words[i]))
