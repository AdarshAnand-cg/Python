# Using Global Variable
count = 1
def count_num(n):
    global count
    if n == count:
        return 1
    print(n)
    return count_num(n-1)
print(count_num(5))

# Without Using Global Variable
def count_num(n):
    if n == 1:
        return 1
    print(n)
    return count_num(n-1)
print(count_num(5))

# More Complexity
count = 0
def fun(n,count):
    if n == count:
        return
    count += 1
    print(count)
    fun(n,count)
fun(4,count)
