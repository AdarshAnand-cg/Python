first_num=int(input("Enter the First Number:"))
second_num=int(input("Enter the Second Number:"))
third_num=int(input("Enter the Third Number:"))
if first_num>=second_num>=third_num or third_num>second_num>=first_num:
    print(f"The Second Largest Number is {second_num}")
elif second_num>first_num>=third_num or third_num>first_num>=second_num:
    print(f"The Second Largest Number is {first_num}")
elif first_num>third_num>=second_num or second_num>third_num>=first_num:
    print(f"The Second Largest Number is {third_num}")