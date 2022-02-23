#!/bin/python3

"""
    Tag: hashmap, list, dp

    Optimizing Box Weights

    A fulfillment associate has a set of items that need to be packed into two boxes. 
    Given an integer array of the item weights (arr) to be packed, divide the items weights
    into two subsets, A and B, for packaging into the associated boxes, which respecting 
    the following conditions:

    -  The intersection of A and B is null. 
    -  The union A and B is equal to the original array. 
    -  The number of elements in subset A is minimal. 
    -  The sum of A's weights is greater than the sum of B's weights. 

    Return the subset A in incresing order where the sum of A's weights is greater than 
    the sum of B's weights. If more than one subset A exists, return the one with the maximal 
    total weight. 

    Example: n=5, arr=[3,7,5,6,2]
    Output= A:[6, 7]
"""

import math
import os
import random
import re
import sys


def minimalHeaviestSetA(arr):
    if not arr:
        return []
    
    sorted_arr = sorted(arr, reverse=True)
    
    a_weight = 0
    b_weight = sum(arr)
    A = []
    i = 0
    while i < len(sorted_arr) and a_weight <= b_weight:
        a_weight += sorted_arr[i]
        b_weight -= sorted_arr[i]
        A.append(sorted_arr[i])
        i+=1
       
    return sorted(A)