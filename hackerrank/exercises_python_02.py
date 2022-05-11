import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    result = round(meal_cost + tip + tax)
    return result

if __name__ == '__main__':
    meal_cost = 15.50

    tip_percent = 15

    tax_percent = 10

    a = solve(meal_cost, tip_percent, tax_percent)
