# Question-11
def calculate(a,b):
    return f"The Sum of {a} and {b} is {a+b}\nThe Difference of {b} from {a} is {a-b}\nThe Product of {a} and {b} is {a*b}\nThe Division of {b} by {a} is {a/b}"
num=calculate(12,8)
print(num)

# Question-12
def count_digit(number):
    count = 0
    number = str(number)

    if number == "0":
        count = 1
    else:
        for ch in number:
            if ch != "-":
                count += 1

    return f"The Number Of Digits in {number} is {count}"

num = count_digit(12365)
print(num)

