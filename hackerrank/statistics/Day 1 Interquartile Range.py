# Objective
# In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

# Task
# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

# Given an array, values, of n integers and an array, freqs, representing the respective frequencies of values's elements, construct a data set, S, where each values[i] occurs at frequency freqs[i]. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

# Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.


import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    arr = [v for v, f in zip(values, freqs) for i in range(f)]    
    arr = sorted(arr)
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n//2] + arr[n//2 - 1]) / 2
        arr1 = arr[:n//2]
        arr2 = arr[n//2:]
        n = len(arr1)
        if n % 2 == 0:
            q1 = (arr1[n//2] + arr1[n//2 - 1]) / 2
            q3 = (arr2[n//2] + arr2[n//2 - 1]) / 2
        else:
            q1 = arr1[n//2]
            q3 = arr2[n//2]
    else:
        median = arr[n//2]
        arr1 = arr[:n//2]
        arr2 = arr[n//2+1:]
        n = len(arr1)
        q1 = arr1[n//2]
        q3 = arr2[n//2]
    interquartile = float(q3 - q1)
    print(round(interquartile, 1))
 
    # Print your answer to 1 decimal place within this function

if __name__ == '__main__':
    #n = int(input().strip())

    #val = list(map(int, input().rstrip().split()))

    #freq = list(map(int, input().rstrip().split()))
    n = 10
    val = [10, 40, 30, 50, 20]
    freq = [1, 2, 3, 4, 5]

    interQuartile(val, freq)