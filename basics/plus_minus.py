import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr: list[int]):
    n = len(arr)
    n_pos = 0
    n_null = 0
    n_neg = 0
    for k in arr:
        if k > 0:
            n_pos += 1
        elif k < 0:
            n_neg += 1
        else:
            n_null += 1
    print(f'{n_pos/n:.6f}\n{n_neg/n:.6f}\n{n_null/n:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
