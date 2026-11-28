# Normal Case
def add(a,b):
    return a+b
print(add(12,13))

# Lambda Function
add = lambda a,b : a+b
print(add(12,13))

# Positive or Negative or zero
number = lambda n : "Positive" if n > 0 else "Negative" if n < 0 else "Zero" 
print(number(12))

# Check whether Palindrome or not
string = lambda string : "Palindrome" if string[:] == string[::-1] else "Not A palindrome"
print(string("racecar"))

# Sorting on the basis of length of characters
words = ["apple", "kiwi", "fig", "guava"]
words = sorted(words, key=lambda word : len(word))
print(words)

# Sorting on the basis of last character
words = sorted(words, key=lambda word : word[-1])
print(words)

# Sorting as per the first character
list = ["zebra", "snake", "camel", "jaguar", "gorilla", "monkey"]
list=map(lambda hello : hello, list)
print(",".join(list))


word = "education"
result = filter(lambda ch : ch in "aeiou",word)
print(", ".join(result))