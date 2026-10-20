# Question-21
def analyze_number(number):
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number

    even = number % 2 == 0
    digits = len(str(absolute_value))

    return absolute_value, even, digits

print(analyze_number(-246))


# Question-22
def calculate_stats(a, b, c):
    return min(a, b, c), max(a, b, c), a + b + c

print(calculate_stats(10, 25, 15))


# Question-23
def make_sentence(subject, verb, object):
    return f"{subject} {verb} {object}."

print(make_sentence(object="Python", subject="I", verb="love"))


# Question-24
def apply_discount(price, discount=0):
    return price - (price * discount / 100)

print(apply_discount(1000))
print(apply_discount(1000, 20))
print(apply_discount(price=2000, discount=15))


# Question-25
def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus

print(calculate_pay(8))
print(calculate_pay(8, 250))
print(calculate_pay(hours=8, bonus=500))
print(calculate_pay(hours=10, rate=300, bonus=1000))


# Question-26
def get_coordinates(x=0, y=0):
    return x, y

print(get_coordinates())
print(get_coordinates(x=10))
print(get_coordinates(y=20))


# Question-27
def compare(a, b):
    if a > b:
        message = "A is greater"
        difference = a - b
    elif b > a:
        message = "B is greater"
        difference = b - a
    else:
        message = "Equal"
        difference = 0

    return message, difference

print(compare(20, 10))
print(compare(10, 20))
print(compare(15, 15))


# Question-28
def convert_temperature(value, scale="C"):
    if scale == "C":
        return (value * 9 / 5) + 32
    else:
        return (value - 32) * 5 / 9

print(convert_temperature(25))
print(convert_temperature(77, "F"))


# Question-29
def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"

print(calculate_result(80))
print(calculate_result(30))
print(calculate_result(60, 70))


# Question-30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return quantity * price + delivery_fee

print(order_summary("Book", 2, 150))
print(order_summary("Book", 2, 150, delivery_fee=20))