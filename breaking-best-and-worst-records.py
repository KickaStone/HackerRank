#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    break_min = 0
    break_max = 0
    for score in scores:
        if score < min_score:
            min_score = score
            break_min += 1
        elif score > max_score:
            max_score = score
            break_max += 1

    return [break_max, break_min]


# Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
