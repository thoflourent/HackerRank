#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    a.sort()
    k = 0
    if len(a) == 1:
        return a[0]
    elif len(a)%2 == 0:
        while 2*k < len(a):
            if a[2*k] != a[2*k+1]:
                return a[2*k]
            k += 1
    else:
        even_a = a[:-1]
        while 2*k < len(even_a):
            if even_a[2*k] != even_a[2*k+1]:
                return a[2*k]
            k += 1
        return a[-1]
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()



