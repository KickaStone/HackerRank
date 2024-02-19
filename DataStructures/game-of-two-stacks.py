#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

'''
# 4 of 10 testcases passed, 2 TLE
def twoStacks(maxSum, a, b):
    # Write your code here
    total = 0
    cnt = 0
    i, j = 0, 0
    while total < maxSum:
        cnt += 1
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                total += a[i]
                i+=1
            else:
                total += b[j]
                j+=1
        elif i < len(a):
            total += a[i]
            i+=1
        elif j < len(b):
            total += b[j]
            j+=1

    if total > maxSum:
        return cnt-1
    else:
        return cnt
'''

#
# def twoStacks(maxSum, a, b):
#     total = 0
#     res = 0
#     i, j = 0, 0
#     cnt1, cnt2 = 0 , 0
#     while i < len(a) and cnt1 <= maxSum:
#         cnt1+=a[i]
#         i+=1
#     while j < len(b) and cnt2 <= maxSum:
#         cnt2 += b[j]
#         j+=1
#
#     print(i, j)
#
#     c = a[:i][::-1] + b[:j]
#     sums = [0]
#     for x in c:
#         sums.append(sums[-1] + x)
#
#     for i in range(len(sums)):
#         for j in range(i+1, len(sums)):
#             if sums[j] - sums[i] < maxSum:
#                 res = max(res, j-i)
#     return res

def twoStacks(maxSum, a, b):
    i, j = -1, -1
    cnt1, cnt2 = 0 , 0
    while i < len(a) and cnt1 <= maxSum:
        i+=1
        cnt1+=a[i]
    while j < len(b) and cnt2 <= maxSum:
        j+=1
        cnt2 += b[j]

    c = a[:i][::-1] + b[:j]
    print(c)

    # slide window
    left, right = 0
    total = 0
    res = 0
    N = len(c)
    while right < N:
        total += c[right]
        while total > maxSum:
            total -= c[left]
            left += 1

        res = max(res, right - left + 1)
        right += 1


"""
another solution -- basically the same idea
def twoStacks(maxSum, stack1, stack2):
    # Initialize variables to track the sum and the count of removed elements
    currentSum, count = 0, 0
    # Initialize pointers for both stacks
    i, j = 0, 0
    # First, try to add as many elements from stack1 as possible without exceeding maxSum
    while i < len(stack1) and currentSum + stack1[i] <= maxSum:
        currentSum += stack1[i]
        i += 1
    # At this point, i is the maximum number of elements we can take from stack1
    count = i
    # Now, try to add elements from stack2, and if necessary, remove some from stack1
    while j < len(stack2) and i >= 0:
        currentSum += stack2[j]
        j += 1
        # If currentSum exceeds maxSum, try removing elements from stack1
        while currentSum > maxSum and i > 0:
            i -= 1
            currentSum -= stack1[i]
        # If currentSum is within maxSum, update the count if it's a better solution
        if currentSum <= maxSum and i + j > count:
            count = i + j
    return count
"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
