#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n = 13
    b = format(n, "b")
    max_ones = 0
    ones = 0
    for i in b:
        if i == '1':
            ones += 1
            if max_ones <= ones:
                max_ones = ones
        else:
            if max_ones <= ones:
                max_ones = ones            
            ones = 0
    print(max_ones)
            
