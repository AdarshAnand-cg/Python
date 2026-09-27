count=total_salaries=0
for i in range(1,9):
    salary=int(input("Enter Your Salary:-"))
    if salary>=100000:
        count+=1
        total_salaries+=salary
        print("Executive")
    elif salary>50000:
        count+=1
        total_salaries+=salary
        print("Senior")
    elif salary>25000:
        count+=1
        total_salaries+=salary
        print("Mid")
    elif salary>0:
        count+=1
        total_salaries+=salary
        print("Junior")
    else:
        print('Invalid Input')
print(f"The Total count of salaries is {count}\nThe Avarage of salaries is {total_salaries/count}")
