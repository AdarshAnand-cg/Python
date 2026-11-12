str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

if len(str1) != len(str2):
    print("Not Anagram")

else:
    flag = True

    for i in str1:
        count1 = 0
        count2 = 0

        for j in str1:
            if i == j:
                count1 += 1

        for k in str2:
            if i == k:
                count2 += 1

        if count1 != count2:
            flag = False

    if flag:
        print("Anagram")
    else:
        print("Not Anagram")