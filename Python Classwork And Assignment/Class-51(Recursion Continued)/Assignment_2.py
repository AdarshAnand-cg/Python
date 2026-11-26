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








