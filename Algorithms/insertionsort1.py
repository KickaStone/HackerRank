#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    t = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] >= t:
        arr[i + 1] = arr[i]
        i -= 1
        print(' '.join(map(str, arr)))
    arr[i + 1] = t
    print(' '.join(map(str, arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
