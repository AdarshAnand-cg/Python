string=input("Enter Any String:-").split()
for ch in range(len(string)):
    for chr in range(len(string)):
        if (string[ch] == string[chr]) or (ch > chr):
            continue
        print(f"{string[ch]}-{string[chr]}")