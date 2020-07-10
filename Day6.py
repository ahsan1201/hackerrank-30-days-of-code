# ask for a string/s, and then print on the same single line, first the even indexes walay number and then odd indexes walay number.


print("Hi there, Let's play a game!")
T = int(input("How many strings will you'd like to play with? :  ")) #T: Number of test cases
InpList = []
for i in range(T):
    print('Enter a string with length between 2 and 10000 characters')
    InpList.append(input('> '))
    if len(InpList[i]) in range(2, 10001):
        continue
    else:
        print('Enter a string with length between 2 and 10000 characters')
        InpList.append(input('> '))


for ii in range(len(InpList)):
    odd = []
    even = []
    for j in range(len(InpList[ii])):
        if j % 2 == 0:
            odd.append(InpList[ii][j])
        else:
            even.append(InpList[ii][j])
    print(''.join(odd) + ' ' + ''.join(even))


