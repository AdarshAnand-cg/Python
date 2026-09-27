first_number=int(input("Enter a number:" ))
second_number=int(input("Enter another number: "))
operators=int(input("Choose the serial number for the desired operation:-\n1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\nSelect an option from above(1/2/3/4):-"))
if operators==1:
    print(f"The Desired Sum is :{first_number+second_number}")
elif operators==2:
    print(f"The Desired Difference is :{first_number-second_number}")
elif operators==3:
    print(f"The Desired Product is :{first_number*second_number}")
elif operators==4:
    print(f"The Desired Sum is :{first_number/second_number}")
else :
    print("Oops!Please Enter The Valid Input\n'Hint' your response is 1/2/3/4.")