score1=int(input("Enter the First Score:"))
score2=int(input("Enter the Second Score:"))
score3=int(input("Enter the Third Score:"))
while score1<0 or score1>100 or score2<0 or score2>100 or score3<0 or score3>100:
    print("Either Score1,score2 or score3 is Out of Range")
    score1=int(input("Enter the First Score:"))
    score2=int(input("Enter the Second Score:"))
    score3=int(input("Enter the Third Score:"))
    
