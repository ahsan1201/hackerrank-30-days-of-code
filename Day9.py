# Recursion
# Factorial question


def factorial(x):

    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


num = 3
print("The factorial of", num, "is", factorial(num))









# ------------------------------------------
# Hacker Rank accepted
# import math
# import os
# import random
# import re
# import sys


# Complete the factorial function below.
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return (n * factorial(n - 1))
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     result = factorial(n)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
