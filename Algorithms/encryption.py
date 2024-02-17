#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    # remove the spaces from the string
    s = s.replace(' ', '')
    # calculate the length of the string
    l = len(s)
    # calculate the number of rows and columns
    r = int(math.floor(math.sqrt(l)))
    c = int(math.ceil(math.sqrt(l)))
    # if the product of the number of rows and columns is less than the length of the string
    if r*c < l:
        # increment the number of rows
        r += 1
    # create a list of strings with length equal to the number of columns
    res = ['']*c
    # iterate through the string
    for i in range(l):
        # add the current character to the string at the index equal to the current index modulo the number of columns
        res[i%c] += s[i]
    # return the strings joined by a space
    return ' '.join(res)

    # my solution:
    # s=s.replace(' ', '')
    # row = int(math.ceil(math.sqrt(len(s))))
    # col = row
    # if (row-1)*col > len(s):
    #     row -= 1
    # res = []
    # for i in range(col):
    #     line = ''
    #     for j in range(row):
    #         line = (line + s[j*col+i]) if j*col+i < len(s) else line
    #     res.append(line)
    # return ' '.join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
