'''
Challenge from : https://www.hackerrank.com/challenges/sock-merchant
Language: Python 3
Simplified solution
'''

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = set(ar)

    return sum([ar.count(color)//2 for color in colors])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
