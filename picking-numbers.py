#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


# O(nlog n) time;O(1) space
# def pickingNumbers(a):
#     a = sorted(a)
#     i, j = 0, 0
#     res = 1
#     while j < len(a):
#         while j < len(a) and a[j] - a[i] <= 1:
#             j += 1
#         res = max(j - i, res)
#         i += 1
#         while i < j and a[i] - a[i - 1] == 0:
#             i += 1
#
#     return res

# dict O(n) time; O(n) space
from collections import Counter
def pickingNumbers(a):
    cnt = Counter(a)
    res = 0
    for x in cnt.keys():
        res = max(res, cnt[x-1]+cnt[x], cnt[x]+cnt[x+1])
    return res




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
