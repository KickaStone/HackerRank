#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    from_start = p // 2
    if n % 2 == 0:
        n = n + 1
    from_end = (n - p) // 2  # if no 'if', 6->5 will be wrong

    return min(from_end, from_start)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
