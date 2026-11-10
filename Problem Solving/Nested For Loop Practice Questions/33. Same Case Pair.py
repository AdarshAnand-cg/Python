string=input("Enter Any String:-")
for i in range(len(string)):
    for j in range(len(string)):
        if (65<=ord(string[i])<=90) and (65<=ord(string[j])<=90):
            print(f"UPPERCASE PAIR = {string[i]}-{string[j]}")
        elif (97<=ord(string[i])<=122) and (97<=ord(string[j])<=122):
            print(f"lowercase pair = {string[i]}-{string[j]}")
    
