# Task
# Given an integer, n, print its first 10 multiples. Each multiple n * 1  (where 1 < 10) should be printed on a new line in the form: n x i = result.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')