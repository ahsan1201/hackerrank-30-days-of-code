inp = int(input('Hi,How many entries you want to add in dictionary?: '))
phoneBook = {}

# for i in range(inp):
#    inp1 = input('Enter the Name of your contact: ')
# phoneBook[inp1] = input('Enter the phone number of the contact: ')

for i in range(inp):
    val_inp = input().split(' ')  # *VALUE* With this line we can get user and his number together, and then separate via space
    phoneBook[val_inp[0]] = val_inp[1]

for j in range(inp):
    inp2 = input('Search your dictionary: ')
    if inp2 in phoneBook:
        print(phoneBook[inp2])
    else:
        print('Not Found')


# #Alternate - HackerRank Accepted Code
# Dasti Comment ALL Shortcut : ctrl + /

# inp = input()
# while len(inp) in range(1, 100001):
#
#     phoneBook = {}
#     inp1 = int(inp)
#     for i in range(inp1):
#         val_inp = input().split(' ')
#         phoneBook[val_inp[0]] = val_inp[1]
#     break
#
# try:
#     while True:
#         inp2 = input()
#         if inp != "":
#             if inp2 in phoneBook:
#                 print(inp2 + '=' + phoneBook[inp2])
#             else:
#                 print('Not found')
#         else:
#             break
# except EOFError:
#     pass
#
# # I still have'nt added a constraint of ensuring a user
# # do not query more than 100000, But khair ...
