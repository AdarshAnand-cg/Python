players = int(input("Enter Players: "))
matches = int(input("Enter Matches: "))

highest = -1
top_player = 0

for i in range(players):
    total = 0

    for j in range(matches):
        runs = int(input("Enter Runs: "))
        total += runs

    print("Player", i+1, "Total Runs =", total)

    if total > highest:
        highest = total
        top_player = i+1

print("Highest Scorer = Player", top_player)
print("Highest Runs =", highest)
