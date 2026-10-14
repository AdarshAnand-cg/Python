for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)

# Output
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4

# Skipped
# A 2
# B 2
