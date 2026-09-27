#<===================>
#Problem-1
#<===================>

#----------------------------#
#IPO(Input,Processing,Output)
#----------------------------#
#INPUT=>First Number
#     =>Second Number
#PROCESSING=>Addition 
#OUTPUT=>Sum Of The two Numbers.

#----------#
#ALGORITHM
#----------#
#Take First number as input
#Take Second number as input
#Perform Addition Operator to sum of the two numbers
#Print the sum of the two numbers.
#Stop.

#=====================#
#With Python Code
#=====================#
first_number=int(input("Enter The First Number:-"))
second_number=int(input("Enter The Second Number:-"))
print(f"The Sum Of the Two Numbers is {first_number+second_number}")

#<===================>
#Problem-2
#<===================>

#----------------------------#
#IPO(Input,Processing,Output)
#----------------------------#
#INPUT=> Any Number
#PROCESSING=>Number Should be Greater than 0
#            Number%2==0(Even)
#            Number%2!=0(Odd) 
#OUTPUT=>Either Even or Odd.

#----------#
#ALGORITHM
#----------#
#Take a number as input
#If number>0:
#    If Modulus of the Number with 2 is equal to 2:
#          Print The Number Is Even.
#    Otherwise :
#          Print The Number Is odd. 
#Otherwise:
#    Print The Number Should Be Greater Than 0 or Check Whether it is even or odd.
#Stop.

#=====================#
#With Python Code
#=====================#
number=int(input("Enter A Number to check whether it is Even or Odd:-"))
if number>0:
    if number%2==0:
        print("The Number Is Even.")
    else:
        print("The Number Is Odd")
else:
    print("Oops! Invalid Input \nFor checking Whether any Number is Odd or Even The number Must Be Zero or Positive")

#<===================>
#Problem-3
#<===================>

#----------------------------#
#IPO(Input,Processing,Output)
#----------------------------#
#INPUT=>First Number
#     =>Second Number
#     =>Third Number
#PROCESSING=> 
#   If First Number>Second Number and Second Number>Third Number
#       print The Largest Number IS First Number
#   If Second Number>First Number and First Number>Third Number
#       print The Largest Number IS Second Number
#   If Third Number>=Second Number and Second Number>=first Number
#       print The LArgest Number IS First Number


#OUTPUT=>The Largest Number Among The Three Numbers.

#----------#
#ALGORITHM
#----------#
#Take First number as input
#Take Second number as input
#Take Third Number as Input
#if First Number>=Second Number and first Number>=Third Number:
#         Print The Largest Number is first Number
#if Second Number>=first Number and Second Number>=Third Number:
#         Print The Largest Number is Second Number
#if  Third Number>=Second Number and Third Number>=First Number:
#         Print The Largest Number is Third Number
#Print the sum of the two numbers.
#Stop.

#=====================#
#With Python Code
#=====================#
first_number=int(input("Enter The First Number:-"))
second_number=int(input("Enter The Second Number:-"))
third_number=int(input("Enter The Third Number:-"))
if first_number>=second_number and first_number>=third_number:
    print(f"The Largest Number Is {first_number}")
if second_number>=first_number and second_number>=third_number:
    print(f"The Largest Number Is {second_number}")
if third_number>=first_number and third_number>=second_number:
    print(f"The Largest Number Is {third_number}")

#<===================>
#Problem-4
#<===================>

#----------------------------#
#IPO(Input,Processing,Output)
#----------------------------#
#INPUT=>Age
#PROCESSING=> 
#   If Age>18:
#       Print They are eligible for vote
#   otherwise:
#       Print Sorry You Are Not Eligible for Vote 

#OUTPUT=>You Are Eligible or Vote Or Not.

#----------#
#ALGORITHM
#----------#
#Take age as Input
#Constraints of Age is 0 to 120
#If Age>18:
#       Print They are eligible for vote
#otherwise:
#       Print Sorry You Are Not Eligible for Vote 
#Stop.

#=====================#
#With Python Code
#=====================#
age=int(input("Enter Your Age :"))
if age>18 and age<120:
    print("You Are Eligible For Voting")
elif age<0:
    print("Oops!You Are Not Eligible For Voting")
else:
    print("Invalid Input")

#<===================>
#Problem-5
#<===================>

#----------------------------#
#IPO(Input,Processing,Output)
#----------------------------#
#INPUT=>Price
#PROCESSING=>
#   Check whether Price is greater than or equal to 2000
#   If Price>=2000:
#       Calculate 20% Discount
#       Subtract Discount from Price
#       Get Final Price
#   otherwise:
#       No Discount is given
#       Final Price remains the same as Price
#
#OUTPUT=>Final Price

#----------#
#ALGORITHM
#----------#
#Take Price as Input
#Constraint of Price is greater than or equal to 0
#
#Understand the condition:
#If Price is greater than or equal to 2000,
#20% discount should be given.
#Otherwise, no discount should be given.
#
#If Price>=2000:
#       Calculate Discount = Price*20/100
#       Calculate Final Price = Price-Discount
#       Print Final Price
#otherwise:
#       Print Price as Final Price
#
#Stop.

#=====================#
#With Python Code
#=====================#

price=float(input("Enter Item Price :"))

if price>=2000:
    discount=price*20/100
    final_price=price-discount
    print("Final Price :",final_price)
else:
    print("Final Price :",price)

#<===================>
#Problem-6
#<===================>

#----------------------------#
#IPO(Input,Processing,Output)
#----------------------------#
#INPUT=>Three Subject Marks
#PROCESSING=>
#   Calculate total marks
#   Calculate average marks
#   Check whether Average is greater than or equal to 40
#   If Average>=40:
#       Print Pass
#   otherwise:
#       Print Fail
#
#OUTPUT=>Average and Pass or Fail

#----------#
#ALGORITHM
#----------#
#Take marks of three subjects as Input
#
#Constraints of Marks:
#   Each subject mark should be between 0 and 100
#
#Understand the condition:
#   First calculate the total of three subject marks
#   Then calculate the average
#   If Average is greater than or equal to 40,
#   the student will Pass.
#   Otherwise, the student will Fail.
#
#Calculate Total:
#       Total=Mark1+Mark2+Mark3
#
#Calculate Average:
#       Average=Total/3
#
#If Average>=40:
#       Print Pass
#otherwise:
#       Print Fail
#
#Stop.

#=====================#
#With Python Code
#=====================#

mark1=float(input("Enter Marks of Subject 1 :"))
mark2=float(input("Enter Marks of Subject 2 :"))
mark3=float(input("Enter Marks of Subject 3 :"))

average=(mark1+mark2+mark3)/3

print("Average :",average)

if average>=40:
    print("Pass")
else:
    print("Fail")


