# Objective
# In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 != 0:
        print("Weird")
    else:
        if N in range(2, 6):
            print("Not Weird")
        elif N in range(6, 21):
            print("Weird")
        elif N > 20:
            print("Not Weird")