# Write first 10 multiples of a table (number  be of user choice)

import math
import os
import random
import re
import sys

# if __name__ == '__main__':
# Indefinitely runs.
while 1:
    n = int(input('Please enter a number between 2 and 20: '))

    if n in range(2, 21):
        for i in range(1, 11):
            print(str(n) + ' x ' + str(i) + ' = ' + str(n * i))
            continue

    else:
        print('please enter a number from the range')
        continue
