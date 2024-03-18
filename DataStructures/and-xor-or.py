#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# def cal(x, y):
#     return ((x & y) ^ (x | y)) & (x ^ y)  # this is equivalent to x xor y.
# def andXorOr(a):
#     # Write your code here
#     stack = []
#     res = 0
#     for x in a:
#         while len(stack) and stack[-1] > x:
#             t = stack.pop()
#             res = max(cal(x, t), res)
#             if len(stack):
#                 res = max(res, cal(stack[-1], t))
#         stack.append(x)
#
#     while len(stack) >= 2:
#         res = max(res, cal(stack.pop(), stack[-1]))
#     return res

# reference : https://www.hackerrank.com/rest/contests/master/challenges/and-xor-or/hackers/mosquis/download_solution
def andXorOr(a):
    stack = [a[0]]
    res = 0
    for i in range(1, len(a)):
        y = a[i]
        while len(stack):
            x = stack.pop()
            res = max(res, x^y)
            if x < y:
                stack.append(x)
                break
        stack.append(y)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
