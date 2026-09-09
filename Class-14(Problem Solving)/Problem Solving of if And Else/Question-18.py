temperature=int(input("Enter the Temperature (in °C):"))
if temperature>35:
    print("Hot")
elif temperature>=26:
    print("Normal")
elif temperature>=16:
    print("Cold")
elif temperature>=0:
    print("Very Cold")
else :
    print("Freezing")
