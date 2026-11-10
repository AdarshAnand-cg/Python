string=input("Enter Any String:-").split()
for i in range(len(string)):
    visited = 0
    for k in range(i):
        if string[i] == string[k]:
            visited = 1
    if visited == 0:
        for j in range(i+1,len(string)):
            if len(string[i])==len(string[j]):
                print(f"The Same Length Word PAir :- {string[i]}-{string[j]}")
    
