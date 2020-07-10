#Arrays
# I give an array, reverse print its items
inp = int(input('Hi,How big of an array you want?: '))

arri = []
for i in range(inp):
    arri.append(int(input('Enter a Number : ')))

rev_arr = arri[::-1]
# print via List
print(arri)
print(rev_arr)

# Method to print a List as " a single line of space-separated numbers"
print(*rev_arr)

