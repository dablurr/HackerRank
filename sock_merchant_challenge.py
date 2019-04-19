'''
Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
Language : Python 3
Simplified solution
'''



import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
  colors = set(ar)

  return sum([ar.count(color)//2 for color in colors])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
