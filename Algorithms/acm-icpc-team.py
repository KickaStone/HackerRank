#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#
from itertools import product

"""

def knownTopics(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            cnt += 1
    return cnt


def acmTeam(topic):
    # Write your code here
    maxKnown, cnt = 0, 0
    idx = [i for i in range(len(topic))]
    for i, j in product(idx, idx):
        if i >= j:
            continue
        known = knownTopics(topic[i], topic[j])
        if known == maxKnown:
            cnt += 1
        elif known > maxKnown:
            maxKnown = known
            cnt = 1

    return maxKnown, cnt
"""
def acmTeam(topic):
    maxKnown, cnt = 0, 0
    idx = [i for i in range(len(topic))]
    for i, j in product(idx, idx):
        if i >= j:
            continue
        known = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')  # bit manipulation
        if known == maxKnown:
            cnt += 1
        elif known > maxKnown:
            maxKnown = known
            cnt = 1

    return maxKnown, cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
