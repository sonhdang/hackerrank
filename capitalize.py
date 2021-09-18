# https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    flag = False
    result = ""
    for c in s:
        if (c.isalpha() or c.isdigit()) and not flag:
            result += c.upper()
            flag = True
        elif c.isspace():
            result += c
            flag = False
        else:
            result += c
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
