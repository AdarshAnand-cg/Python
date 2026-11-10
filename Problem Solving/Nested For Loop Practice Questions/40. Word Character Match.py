sentence=input("Enter Any String:-").split()
for i in range(len(sentence)):
    for j in range(i+1, len(sentence)):
        visited=0

        for ch in sentence[i]:
            for chr in sentence[j]:
                if ch == chr:
                    visited=1

    if visited == 1:
        print(f"{sentence[i]-{sentence[j]}}")
        

