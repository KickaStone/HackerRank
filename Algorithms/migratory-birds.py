#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # return Counter(sorted(arr)).most_common(1)[0][0] # This is the most pythonic way to solve this problem, but it's not the most efficient

    cnt = {}
    for i in arr:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    return max(cnt, key=lambda x: (cnt[x], -x)) # This is the most efficient way to solve this problem



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
