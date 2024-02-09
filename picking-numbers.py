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

def pickingNumbers(a):
    a = sorted(a)
    i, j = 0, 0
    res = 1
    while j < len(a):
        while j < len(a) and a[j] - a[i] <= 1:
            j += 1
        res = max(j - i, res)
        i += 1
        while i < j and a[i] - a[i - 1] == 0:
            i += 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
