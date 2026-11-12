board = ["-"] * 9

print("Enter Board Values: X, O or -")
for i in range(3):
    for j in range(3):
        value = input("Enter Value: ")
        if value == "x" or value == "X":
            board[i*3+j] = "X"
        elif value == "o" or value == "O":
            board[i*3+j] = "O"
        else:
            board[i*3+j] = "-"

winner = ""

for i in range(3):
    if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != "-":
        winner = board[i*3]

    if board[i] == board[i+3] == board[i+6] and board[i] != "-":
        winner = board[i]

if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]

if board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]

if winner != "":
    print(winner, "Wins")
else:
    empty = 0
    for i in range(9):
        if board[i] == "-":
            empty += 1

    if empty > 0:
        print("Game Incomplete")
    else:
        print("Draw")
