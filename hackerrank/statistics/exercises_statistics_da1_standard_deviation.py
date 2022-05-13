import random
import re
import sys

    # Print your answers to 1 decimal place within this function
def stdDev(arr):
    mean = sum(arr) / len(arr)
    variance = sum([(x - mean) ** 2 for x in arr]) / len(arr)
    return round(math.sqrt(variance), 1)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
