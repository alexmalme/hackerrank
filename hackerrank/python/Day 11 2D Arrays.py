
import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
       
    max_hourglass = []
    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            max_hourglass.append(s)

    print(max(max_hourglass))