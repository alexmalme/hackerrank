import math
import os
import random
import re
import sys


def weightedMean(X, W):
    result = round(sum([x*w for x, w in zip(X, W)])/sum(W), 1)
    return result
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
