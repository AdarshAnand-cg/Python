# ____________________________________________
# ________________Question-1__________________
def even_place_sum(n):
    if n == 0:
        return 0
    return (n // 10)%10 + even_place_sum(n // 100)
print(even_place_sum(583246))

# ____________________________________________
# ________________Question-2__________________
def reverse_the_number(n):
    if n == 0:
        return 0
    print( n % 10,end="")
    return reverse_the_number(n//10)
reverse_the_number(4827)
print()

# ____________________________________________
# ________________Question-3__________________
def check_palindrome(n):
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return check_palindrome(n[1:-1])
    return False
print(check_palindrome("level"))

# ____________________________________________
# ________________Question-4__________________
def count_character(word,count):
    if len(word) == 0:
        return 0
    if word[0] == count:
        return 1+count_character(word[1:],count)
    else:
        return count_character(word[1:],count)
print(count_character("programming","m"))

# ____________________________________________
# ________________Question-5__________________
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6

# ____________________________________________
# ________________Question-6__________________
def check_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return check_prime(n, i + 1)

print(check_prime(17))  

# ____________________________________________
# ________________Question-7__________________
def occurence_of_character(word,letter):
    if word == "":
        return ""
    if word[0] != letter:
        print(word[0],end="")
    return occurence_of_character(word[1:],letter)
print(occurence_of_character("mississippi","s"))


# ____________________________________________
# ________________Question-8__________________
a = ""
def change_binary(n):
    global a
    if n <= 0:
        return 
    
    change_binary(n // 2)
    print(n % 2,end="")
change_binary(13)
print()

# ____________________________________________
# ________________Question-9__________________
result = True
def contains_string(n):
    global result
    if n == "":
        return False
    contains_string(n[1:])
    if 48<=ord(str(n[0]))<=57:
        return result
    else:
        result = False
    return result
print(contains_string("1234565jjh43"))

# ____________________________________________
# ________________Question-10_________________
a = 0
def sum_to(n):
    global a
    if n < 10:
        return n
    a = n%10 + sum_to(n//10)
    return a%10 + sum_to(a // 10)
print(sum_to(9975))


















