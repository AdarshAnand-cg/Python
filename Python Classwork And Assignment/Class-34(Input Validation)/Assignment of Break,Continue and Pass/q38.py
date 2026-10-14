for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

# OUTPUT
# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed
