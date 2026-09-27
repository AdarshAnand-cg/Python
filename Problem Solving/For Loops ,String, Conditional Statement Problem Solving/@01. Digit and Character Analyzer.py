string="AdarSh 1234 @#$%"
count_upper=0
count_lower=0
count_digit=0
count_spaces=0
count_special_character=0
for ch in string:
    if ch>="A" and ch<="Z":
        count_upper+=1
    elif ch>="a" and ch<="z":
        count_lower+=1
    elif ch>=0 and ch<=9:
        count_digit+=1
    elif ch=="":
        count_spaces+=1
    else:
        count_special_character+=1

highest_value=count_upper
if count_lower>highest_value:
    highest_value=count_lower
if count_digit>highest_value:
    highest_value=count_digit
if count_spaces>highest_value:
    highest_value=count_spaces
if count_special_character>highest_value:
    highest_value=count_special_character

same_value=count_upper
if count_lower==same_value:
    highest_value



