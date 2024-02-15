#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

# def squares(a, b):
#     start = int(math.sqrt(a))
#     if start**2 != a:
#         start +=1
#     cnt = 0
#     while start**2 <= b:
#         cnt += 1
#         start += 1
#     return cnt

def squares(a, b):
    return int(math.sqrt(b)) - int(math.sqrt(a - 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
