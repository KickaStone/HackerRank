#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
# def inorder(indexes, root, depth, q, path):
#     if root != -1:
#         left = indexes[root - 1][0]
#         right = indexes[root - 1][1]
#         if (depth + 1) % q == 0:
#             indexes[root - 1][0] = right
#             indexes[root - 1][1] = left
#         inorder(indexes, indexes[root - 1][0], depth + 1, q, path)
#         path.append(root)
#         inorder(indexes, indexes[root - 1][1], depth + 1, q, path)
#
#
# def swapNodes(indexes, queries):
#     res = []
#     for q in queries:
#         path = []
#         inorder(indexes, 1, 1, q, path)
#         res.append(path)
#     return res

# The last testcase exceeds the limit of Python recursion.
# solution: 1. use sys.setrecursionlimit(10000) to unlock the limitation.
# 2. use stack / deque to work around

def inorder(indexes, root, depth, q, path):
    if root == -1:
        return
    if depth % q == 0:
        indexes[root-1][0], indexes[root-1][1] = indexes[root-1][1], indexes[root-1][0]
    inorder(indexes, indexes[root-1][0], depth+1, q, path)
    path.append(root)
    inorder(indexes, indexes[root-1][1], depth+1, q, path)

def swapNodes(indexes, queries):
    result = []
    for q in queries:
        path = []
        inorder(indexes, 1, 1, q, path)
        result.append(path)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
