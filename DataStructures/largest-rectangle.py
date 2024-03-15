#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#
#
# def largestRectangle(h):
#     max_areas = []
#     for i in range(len(h)):
#         minvalue = h[i]
#         max_area = h[i]
#         if i > 0 and h[i] <= h[i-1]:
#             continue
#         for j in range(i, len(h)):
#             l = j - i + 1
#             minvalue = min(minvalue, h[j])
#             max_area = max(max_area, l*minvalue)
#         max_areas.append(max_area)
#     return max(max_areas)

def largestRectangle(h):
    stack = []
    max_area = 0
    for i, x in enumerate(h):
        if len(stack) == 0 or stack[-1][0] <= x:
            stack.append((x, i, 0))
        else:
            cnt = 0
            while len(stack) > 0 and stack[-1][0] > x:
                cur = stack.pop()
                max_area = max((i - cur[1] + 1 + cur[2]) * cur[0], max_area)
                cnt += 1
            stack.append((x, i, cnt))

    while len(stack) > 0:
        cur = stack.pop()
        max_area = max((len(stack) - cur[1] + cur[2]) * cur[0] , max_area)
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
