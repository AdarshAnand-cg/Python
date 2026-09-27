fail_count=0
pass_count=0
good_count=0
excellent_count=0

for a in range(0,10):
    marks=int(input("Enter Your Marks:-"))
    if marks>74:
        print("Excellent")
        excellent_count+=1
    elif marks>49:
        print("Good")
        good_count+=1
    elif marks>=35:
        print("Pass")
        pass_count+=1
    elif marks>=0:
        print("Fail")
        fail_count+=1
    else:
        print("Invalid Input")

print(f"Total Number of Fail Students are {fail_count}")
print(f"Total Number of Pass Students are {pass_count}")
print(f"Total Number of Good Students are {good_count}")
print(f"Total Number of Excellent Students are {excellent_count}")