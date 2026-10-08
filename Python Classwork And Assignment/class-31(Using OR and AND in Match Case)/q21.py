choice = int(input("Enter choice: "))

temperature = float(input("1.Celcius to Fahrenheit\n2.Fahrenheit to Celsius\nEnter temperature: "))

match choice:
    case 1:
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature =", fahrenheit, "F")

    case 2:
        celsius = (temperature - 32) * 5 / 9
        print("Temperature =", celsius, "C")

    case _:
        print("Invalid choice")