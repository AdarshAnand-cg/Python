# Question-1
add = lambda a,b : a+b
print(add(10,20))

# Question-2
square = lambda n:n**2 
print(square(12))

# Question-3
cube = lambda k:k**3
print(cube(3))

# Question-4
check_Even_or_Odd = lambda a :"Even Number" if a % 2 == 0 else "Odd Number"
print(check_Even_or_Odd(12))

# Question-5
greater_number = lambda a,b : f"{a} is Greater Than {b}" if a>b else f"{b} is Greater Than {a}"
print(greater_number(15,67))

# Question-6
convert_celsius_into_Fahrenheit = lambda celsius :(celsius * 9/5) + 32
print(convert_celsius_into_Fahrenheit(25))

# Question-7
length_String = lambda length : len(length)
print(length_String("python"))

# Question-8
uppercase = lambda string : string.upper()
print(uppercase("hello world"))

# Question-9
last_character = lambda string : string[-1]
print(last_character("coding"))

# Question-10
reduced_price = lambda price,discount : price - (price*discount/100)
print(reduced_price(1200,10))
