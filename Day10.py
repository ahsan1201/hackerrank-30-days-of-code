# BinaryNumbers
# BinaryNumbers
from math import floor

n = int(input('Base-10 to Base-2: '))
# temp = 100
list1 = []
while n > 0:
    n1 = list1.append(n % 2)  # Gives remainder (used for bits -> save in list)
    n = floor(n / 2)  # Gives quotient ( Used for further division )

# Solution: If you want to present the conversion
# rev_list = list1[::-1]
# print(*rev_list)
max_1 = 0
ans=1
for i in range(len(list1)):
    if list1[i] == 1:
        max_1 = max_1+1
        if max_1 > ans:
             ans = max_1
        else:
            continue
    else:
        max_1 = 0
        continue

print("Highest No of consec 1's is: " + str(ans))







