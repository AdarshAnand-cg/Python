words = input("Enter Words: ").split()

highest = -1
word1 = ""
word2 = ""

for i in range(len(words)):
    for j in range(i+1, len(words)):
        common = 0

        for k in range(len(words[i])):
            visited = 0
            for x in range(k):
                if words[i][k] == words[i][x]:
                    visited = 1

            if visited == 0:
                for y in words[j]:
                    if words[i][k] == y:
                        common += 1
                        break

        if common > highest:
            highest = common
            word1 = words[i]
            word2 = words[j]

if word1 != "":
    print(word1, "and", word2, "have maximum common characters:", highest)
else:
    print("Enter At Least Two Words")
