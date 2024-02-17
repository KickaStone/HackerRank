#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # using dynamic programming
    # create a list of n elements with value 0
    dp = [0]*len(c)
    # iterate through the list
    for i in range(1, len(c)):
        # if the current cloud is not a thunder cloud
        if c[i] != 1:
            # if the current cloud is the second cloud
            if i == 1:
                # the number of jumps to reach the second cloud is 1
                dp[i] = 1
            else:
                # the number of jumps to reach the current cloud is the minimum of the number of jumps to reach the previous cloud plus 1 and the number of jumps to reach the cloud two steps back plus 1
                dp[i] = min(dp[i-1], dp[i-2]) + 1
        else:
            dp[i] = float('inf')
    # return the number of jumps to reach the last cloud
    return dp[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
