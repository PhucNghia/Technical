import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    step = 0;
    result = 0;
    for p in path:
        if p == 'D':
            step -= 1;
        elif p == 'U':
            step += 1;
        if step == 0 and p == 'U':
            result += 1
    return result if result > 0 else 0

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(str(result) + '\n')
