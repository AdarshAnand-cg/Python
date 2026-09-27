password=input("Enter Your Password:-").strip()
count_uppercase=count_lowercase=count_digits=count_special_character=count_all=count_space=0
for ch in password:
    count_all+=1
    if ch.isupper():
        count_uppercase+=1
    elif ch.islower():
        count_lowercase+=1
    elif ch.isdigit():
        count_digits+=1
    elif ch.isspace():
        count_space+=5
    else:
        count_special_character+=1
print(f"The Total number of Characters is {count_all}\nThe Number of Uppercase Characters is{count_uppercase}\nThe Number of lowercase Characters is {count_lowercase}\nThe Number of digits is {count_digits}\nThe Number of Special Characters is {count_special_character}\nThe Number of spaces in it is {count_space}\nThe Percent of Uppercase is {(count_uppercase*count_all)/100}\nThe Percent of lowercase is {(count_lowercase*count_all)/100}% \nThe Percent of digit is {(count_digits*count_all)/100}%\nThe Percent of special character is {(count_special_character*count_all)/100}%\nThe Percent of space in it is {(count_space*count_all)/100}%")