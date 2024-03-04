#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def nextPrime(N):
    # Base case
    if N <= 1:
        return 2

    prime = N
    found = False

    # Loop continuously until isPrime returns
    # True for a number greater than n
    while not found:
        prime = prime + 1

        if isPrime(prime):
            found = True

    return prime


def waiter(number, q):
    p = 1
    stackA = []
    stackB = []
    answer = []
    for i in range(q):
        p = nextPrime(p)
        while len(number):
            x = number.pop()
            if x % p == 0:
                stackB.append(x)
            else:
                stackA.append(x)
        answer.extend(stackB[::-1])
        stackB = []
        number = stackA
        stackA = []
    answer.extend(number[::-1])
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    try:
        result = waiter(number, q)
    except Exception as e:
        print(e)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
