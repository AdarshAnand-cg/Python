temperature = int(input("Enter Any Temperature: "))
while temperature < -20 or temperature > 45:
    print("Error!\nInvalid Temperature\nPlease Enter Temperature Again:")
    temperature = int(input("Enter Any Temperature: "))
print(temperature)
        
    


