even=0
odd=0
for i in range(0,5):
    number=int(input("Enter Any Number:"))
    string=str(number)
    
    for ch in string:
        digit=int(ch)
        if digit%2==0:
            even+=1
        else:
    
            odd+=1
even+=0
odd+=0
if even>odd:
    print(f"The Number of Even Digits Are {even}\nThe Number of Odd Digits Are {odd}\n The number of Even Digits is greater than Odd digits")
elif odd>even:
    print(f"The Number of Even Digits Are {even}\nThe Number of Odd Digits Are {odd}\nThe number of Odd Digits is greater than Even digits")
else:
    print(f"The Number of Even Digits Are {even}\nThe Number of Odd Digits Are {odd}\nThe number of Odd Digits is Equal to Even digits")