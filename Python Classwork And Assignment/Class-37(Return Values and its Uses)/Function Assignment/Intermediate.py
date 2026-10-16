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

# Question-13
def classify_number(number):
    if number>0:
        return "Positive"
    elif number==0:
        return "Zero"    
    else:
        return "Negative"
Number=classify_number(34)
print(Number)

# Question-14
def calculate_total(price,quantity=1):
    return f"The Price of the products : Rs{price}/-\nQuantity: {quantity}"
total=calculate_total(12200,4)
print(total)

# Question-15
def create_email(username,domain="example.com"):
    return f"Email Address: {username+domain}"
email=create_email("adarsh.anad.cg@gmail",".com")
print(email)

# Question-16
def format_name(first, last, uppercase=False):
    name = first + " " + last
    if uppercase == True:
        return name.upper()
    return name

print(format_name("Adarsh", "Anand"))
print(format_name("Adarsh", "Anand", True))


# Question-17
def percentage(marks, total=100):
    return (marks / total) * 100

print(percentage(85))
print(percentage(450, 500))


# Question-18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

print(convert_minutes(5))
print(convert_minutes(10, 60))


# Question-19
def student_details(name, age, city):
    return f"Name: {name}, Age: {age}, City: {city}"

print(student_details(city="Muzaffarpur", age=18, name="Adarsh"))


# Question-20
def bill(item, quantity=1, price=100):
    return f"Bill Amount of {item}: {quantity * price}"

print(bill("Pen", 5, 10))
print(bill(item="Book", quantity=3, price=50))
