username = input("Enter username: ").strip()

while len(username) < 5 or " " in username:
    print("Invalid username! Please try again.")
    username = input("Enter username: ").strip()

print("Accepted username:", username)