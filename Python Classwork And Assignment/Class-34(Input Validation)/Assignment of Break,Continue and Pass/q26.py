for x in range(3):
    continue
else:
    print("A")

# OUTPUT
# A

for x in range(3):
    break
else:
    print("B")

# OUTPUT
# 

for x in range(0):
    print(x)
else:
    print("C")

# OUTPUT
# C
