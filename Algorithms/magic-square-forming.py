#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def rotate(matrix):
    return list(zip(*matrix[::-1]))


def reflect(matrix):
    return [row[::-1] for row in matrix]


def generate_magic_squares():
    base_solution = [[2, 7, 6],
                     [9, 5, 1],
                     [4, 3, 8]]

    solutions = [base_solution]
    for _ in range(3):
        base_solution = rotate(base_solution)
        solutions.append(base_solution)

    reflected_base_solution = reflect(base_solution)
    solutions.append(reflected_base_solution)
    for _ in range(3):
        reflected_base_solution = rotate(reflected_base_solution)
        solutions.append(reflected_base_solution)

    return solutions


def cost(s, t):
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += abs(s[i][j] - t[i][j])
    return sum


def formingMagicSquare(s):
    magic_squares = generate_magic_squares()
    return min([cost(s, ms) for ms in magic_squares])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
