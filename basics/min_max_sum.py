#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr: list[int]):
    arr = sorted(arr)
    min = sum(arr[0:4])
    max = sum(arr[1:5])
    print(f'{min} {max}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)