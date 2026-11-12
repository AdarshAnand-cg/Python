string = input("Enter Words: ").split()

for word in string:
    a = 0
    b = len(word)-1
    c = True
    while a < b:
        if word[a] != word[b]:
            c=False
            break
        a+=1
        b-=1
    if c:
        print("(❁ ´◡`❁)",word,"is Palindrome","(❁ ´◡`❁)") 
