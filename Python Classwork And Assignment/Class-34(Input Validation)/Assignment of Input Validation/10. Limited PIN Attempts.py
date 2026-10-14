secret_PIN=2468
count=1
while count<=3:
   enter_PIN=int(input("Enter The PIN:-"))
   if secret_PIN==enter_PIN:
      print("Correct PIN")
      break
   else:
      count+=1
      print(f"Wrong PIN\n{4-count} Attempts Left")
      pass
if count>3:
    print("Access Denied")

    
