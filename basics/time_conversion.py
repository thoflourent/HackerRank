#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# format : hh:mm:ssAM
#

def timeConversion(s: str)-> str:
    time = datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")
    return time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()