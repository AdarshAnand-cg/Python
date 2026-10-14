count=0
while True:
    number=int(input("Guess The Number:\nEnter Any Number:-"))
    if number>0:
        print(number)
        count+=1
        print(f"Serial Number Of Attempts:-{count}")
        pass
    if number==0:
        print("You Found The Chosen Number")
        break
    if number<0:
        continue

