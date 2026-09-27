# Print
# *       *
# *       *
# *       *
# *       *
# *       *
# * * * * *

a=""
for i in range(0,5):
    for k in range(0,5):
        if i>=0 and i<4:
            if k==0 or k==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
# Print
# * * * * *
# *       *
# *       *
# *       *
# *       *
# * * * * *

for a in range(5):
    for b in range(5):
        if a==0 or a==4 or a==2:
            print("*",end=" ")
        else:
            if a==1 and b==4:
                print(" ",end="")
            elif a==3 and b==0:
                print(" ",end="")

            if a==1 and b==0:
                print("*",end="")
            if a==3 and b==3:
                print("       *",end="")
            

            # if b==0 or b==4:
            #     print(" ",end=" ")
            # else:
            #     print(" ",end=" ")
    print()
# Print
# *       *
# *       *
# *       *
# *       *
# *       *
# * * * * *
