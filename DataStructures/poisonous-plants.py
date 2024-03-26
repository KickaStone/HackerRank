#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    s = [] # stack create
    ans = 0
    for x in p:
        max_day = 0
        while s and x <= s[-1][0]:
            day = s.pop()[1]
            max_day = max(max_day, day)

        if s:
            s.append((x, max_day+1))
            ans = max(ans, max_day+1)
        else:
            s.append((x, 1))

    return ans

## [WA]
# def poisonousPlants(p):
#     minima = [p[0]]
#     ans = 0
#     cnt = 0
#     old = p[0]
#     for i in range(1, len(p)):
#         if p[i] <= minima[-1]:
#             ans = max(ans, cnt)
#             cnt = 0
#             minima.append(p[i])
#             old = minima[-1]
#         else:
#             if old == minima[-1]:
#                 cnt = 1
#             if p[i] < old:
#                 cnt += 1
#             old = p[i]
#         print(cnt)
#     return max(ans, cnt)

# def poisonousPlants(p):
#     s = [[p[0], 0]]
#     ans = 0
#     for i in range(1,len(p)):
#         cnt = 0
#         if p[i] > s[-1][0]:
#             s.append((p[i], 0))
#         else:
#             # while len(s) >= 2 and s[-1][0] > s[-2][0]:
#             while len(s) >= 2 and s[-1][0] > s[-2][0] and s[-1][1] <= s[-2][1]:
#                 t = s.pop()
#                 ans = max(ans, t[1])
#                 s[-1][1] += 1
#             s.append([p[i], 0])
#
#     while len(s) >= 2 and s[-1][0] > s[-2][0]:
#         t = s.pop()
#         ans = max(ans, t[1])
#         s[-1][1] += 1
#
#     return max(ans, max([x for num, x in s]))
#
# def poisonousPlants(p):
#     s = [(p[0], 0)]
#     ans = 0
#     for i in range(1, len(p)):
#         if p[i] > s[-1][0]:
#             s.append((p[i], 1))
#         else:
#             max_step = 0
#             while len(s) >= 2 and s[-1][0] > s[-2][0] and s[-1][1] <= s[-2][1]:
#                 max_step = max(max_step, s[-1][1])
#                 ans = max(ans, max_step)
#                 s.pop()
#             if s[-1][0] >= p[i]:
#                 s.append((p[i], 0))
#             else:
#                 s.append((p[i], max_step+1))
#
#         while len(s) >= 2 and s[-1][0] > s[-2][0]:
#             ans = max(ans, s.pop()[1])
#     return ans




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = poisonousPlants(p)
    fptr.write(str(result) + '\n')
    fptr.close()
