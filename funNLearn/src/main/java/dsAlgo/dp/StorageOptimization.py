#!/bin/python3

"""
    Tag: math, dp

    A company is experimenting with flexible storage system for their warehouses. 
    The storage unit consists of a shelving system which is one meter deep with removable
    vertical and horizontal separators. When all separators are installed, each storage space
    is one cubic meter (1' x 1'x 1'). Determine the volume of the largest space when a series 
    of horizontal and vertical separators are removed. 

    Example:
    n = 6, m = 6, h = [4], v = [2]
    return: 4
"""

import math
import os
import random
import re
import sys


from typing import List

def get_longest_continuous_series_length(arr: List[int])-> int:
    longest_length = 0    
    curr_len = 0
    _a = sorted(arr)
    for i in range(len(_a)):
        if i == 0:
            curr_len = 1
        elif _a[i] - _a[i-1] == 1:
            curr_len += 1
        else:
            curr_len = 1
        longest_length = max(longest_length, curr_len)
        
    return longest_length

def storage(n, m, h, v):
    # longest continuous horizontal line removals
    LCHLR = get_longest_continuous_series_length(h)
    # longest continuous vertical line removals
    LCVLR = get_longest_continuous_series_length(v)
    
    return (LCHLR+1) * (LCVLR+1)


assert(storage(2, 2, [1], [2]) == 4)
assert(storage(3, 2, [1, 2, 3], [1, 2]) == 12)
print("Tests Passed!")
