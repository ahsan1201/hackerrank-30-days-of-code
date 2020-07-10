#!/bin/python3
# from hacker rank
import math
import os
import random
import re
import sys


def _get_hourglass_sum(matrix, row, col):
    sum = 0
    sum += matrix[row - 1][col - 1]
    sum += matrix[row - 1][col]
    sum += matrix[row - 1][col + 1]
    sum += matrix[row][col]
    sum += matrix[row + 1][col - 1]
    sum += matrix[row + 1][col]
    sum += matrix[row + 1][col + 1]
    return sum


if __name__ == '__main__':
    arr = []

    for arr_i in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -63
    for i in range(1, 5):
        for j in range(1, 5):
            curr_sum = _get_hourglass_sum(arr, i, j)
            if curr_sum > max_sum:
                max_sum = curr_sum

    print(max_sum)