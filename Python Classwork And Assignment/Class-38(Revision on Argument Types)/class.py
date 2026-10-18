def greet(name):
    print("count", name)

greet("Asha")
greet("Rahul")

# count Asha
# count Rahul

def subtract(a, b):
    return a - b

print(subtract(8, 3))
print(subtract(3, 8))

# 5
# -5

def counter_fun(count):
    count=count+1
    if(count==2):
        return count-19
    return counter_fun(count)
print(counter_fun(-19))
