#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores: list[int]) -> list[int]:
    min, max = scores[0], scores[0]
    min_count, max_count = 0, 0
    n = len(scores)
    for k in range(1,n):
        if scores[k] > max:
            max = scores[k]
            max_count += 1
        elif scores[k] < min:
            min = scores[k]
            min_count += 1
    return [max_count, min_count]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
