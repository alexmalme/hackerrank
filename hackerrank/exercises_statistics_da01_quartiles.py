#Task
# Given an array, arr, of n integers, calculate the respective first quartile (Q1), 
# second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.


import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr = sorted(arr)
    n = len(arr)
    if n % 2 == 0:
        median = int((arr[n//2] + arr[n//2 - 1]) / 2)
        arr1 = arr[:n//2]
        arr2 = arr[n//2:]
        n = len(arr1)
        if n % 2 == 0:
            q1 = int((arr1[n//2] + arr1[n//2 - 1]) / 2)
            q3 = int((arr2[n//2] + arr2[n//2 - 1]) / 2)
        else:
            q1 = int(arr1[n//2])
            q3 = int(arr2[n//2])
    else:
        median = int(arr[n//2])
        arr1 = arr[:n//2]
        arr2 = arr[n//2:]
        n = len(arr1)
        q1 = int(arr1[n//2])
        q3 = int(arr2[n//2])
    return q1, median, q3



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
