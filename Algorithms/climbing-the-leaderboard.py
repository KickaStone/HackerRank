#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

from bisect import *

sys.setrecursionlimit(10000)


def climbingLeaderboard(ranked, player):
    res = []
    keys = list(sorted(set(ranked)))

    for s in player:
        pos = bisect_left(keys, s)
        if pos < len(keys) and keys[pos] == s:
            res.append(len(keys) - pos)
        else:
            keys.insert(pos, s)
            res.append(len(keys) - pos)
        # print(f'{keys}, the rank of {s} is {len(keys)-pos}')
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
