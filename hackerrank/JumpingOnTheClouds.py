#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    result = 0
    index = 0
    i = 0
    check = True
    while i < n-1:
        while c[i] == 0:
            # index += 1
            i += 1
            check = False

        # i = index
        i += 1 if check else i
        check = True
        index = 0
        result += 1
    return result

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(n, c)
    print(str(result) + '\n')
