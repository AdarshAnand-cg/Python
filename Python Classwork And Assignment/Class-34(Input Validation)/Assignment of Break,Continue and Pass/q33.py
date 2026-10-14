for i in range(1, 5):
    if i == 3:
        pass
    print(i)

# 1
# 2
# 3
# 4

for i in range(1, 5):
    if i == 3:
        continue
    print(i)

# OUTPUT
# 1
# 2
# 4