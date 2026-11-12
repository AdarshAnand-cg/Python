str=input("Enter The String:-")
result=""
for ch in range(len(str)):
    if result==True:
        for k in range(len(str)//2):
            i=0
            j=len(str)//2-1
            s=True
            while i<j:
                if str[i] == str[j]:
                    i+=1
                    j-=1
                else:
                    s=False
                    i=j
            if s:
                print(f"{str} is Palandrome")
            else:
                print(f"{str} is not A Palandrome")

        for l in range(len(str)//2,len(str)+1):
                    a=0
                    b=len(str)//2-1
                    c=True
                    while a<b:
                        if str[a] == str[b]:
                            i+=1
                            j-=1
                        else:
                            s=False
                            i=j
                    if s:
                        print(f"{str} is Palandrome")
                    else:
                        print(f"{str} is not A Palandrome")
                    
                    




# string=input("Enter Any Word:-").lower()
# i=0
# j=len(string)-1
# s = True
# while i<j:
#     if string[i]==string[j]:
#         i+=1
#         j-=1
#     else:
#         s=False
#         i=j
# if s:
#     print(f"{string} is Palandrome")
# else:
#         print(f"{string} is not A Palandrome")