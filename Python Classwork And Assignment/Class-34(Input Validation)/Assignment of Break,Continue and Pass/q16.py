n = 0

while n < 5:
    if n == 3:
        continue
    n += 1
    print(n)

# OUTPUT
# 1
# 2
#                                                  =>  ....Kind Of Infinite Loop

# Corrected Version Of The Code
n=0
while n < 5:
    n+=1
    if n == 3:
        continue
    print(n)

    
    
    