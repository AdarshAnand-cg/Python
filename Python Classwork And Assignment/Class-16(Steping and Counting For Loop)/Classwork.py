num=int(input("Enter any number to check whether it is prime or not: "))
for i in range(1,num):
    h=num%i
    if h==0:

        print("This is Prime Number")

Name=(input("Enter a word:")).lower().strip()
length=len(Name)
sum=""
for number in range(length-1,-1,-1):
    sum=sum+Name[number]

if Name==sum:
    print("This Word is Palandrom")
else :
    print("THis word isn't Palandrome")
