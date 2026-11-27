# Question-1
def print_message(message,n):
    if n == 1:
        return message
    print(message)
    return print_message(message,n-1)
print(print_message("Hello",3))

# Question-2
def even_number(n):
    if n == 2:
        return n
    if n % 2 == 0:
        print(n)
    return even_number(n-1)
print(even_number(10))

# Question-3
def sum_odd(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return n + sum_odd(n-1)
    return sum_odd(n-1)
print(sum_odd(10))

#  Question-4
count = 0
def count_number(number,target):
    global count
    if number == 0:
        return 0
    if number%10 == target:
        count += 1
    count_number(number//10,target)
    return count
print(count_number(52525,5))

# Question-5
def product(a):
    if a == 0:
        return 1
    return a%10 * product(a // 10)
print(product(234))

# Question-6
def first_digit(a):
    if a < 10:
        return a
    return first_digit(a // 10)
    
print(first_digit(5837))

# Question-7
status = False
def check_digit(number,target):
    global status
    if number == 0:
        return 0
    if number%10 == target:
        status = True
    check_digit(number//10,target)
    return status
print(check_digit(4826,2))

# Question-8
Count = 0
def length_string(n):
    global Count
    if n == "":
        return ""
    if n[0]:
        Count += 1
    length_string(n[1:])
    return Count
print(length_string("coding"))

# Question-9
Count = 0
def length_string(n):
    global Count
    if n == "":
        return ""
    if n[0] in "aeiouAEIOU":
        Count += 1
    length_string(n[1:])
    return Count
print(length_string("education"))

# Question-10
def check_palindrome(n):
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return check_palindrome(n[1:-1])
    return False
print(check_palindrome("racecar"))