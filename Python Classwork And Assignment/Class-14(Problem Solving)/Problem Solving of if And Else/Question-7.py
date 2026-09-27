num=int(input("Enter Any Number"))
if num%3==0 and num%7==0:
    print("It is Divisible By both 3 and 7")
elif num%3==0:
    print("It is Divisible by 3 Only")
elif num%7==0:
    print("It is Divisible by 7 Only")
else :
    print("Divisible By None.")
