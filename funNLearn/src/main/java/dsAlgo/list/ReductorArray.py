"""
    tag: list, comparator value, reductor array

    Reductor Array 
    For two integer arrays, the comparator value is the total number of elements 
    in the first array such that there exists no integer in the second array with 
    an absolute difference less than or equal to d. Find the comparator value. 

    For example there are two arrays a = [7, 5, 9], b = [13, 1, 4], and the 
    integer d = 3. The absolute difference of a[0]to b[0] = |7 - 13| = 6, 
    b[1] = |7 - 1| = 6, and b[2] =[7- 4] = 3, to recap, the values are 6, 6, 3. 
    In this case, the absolute difference with b[2] is equal to d = 3, so this 
    element does not meet the criterion. 
    
    A similar analysis of a[1] = 5 yields absolute differences of 8, 4, 1 and 
    of a[2] = 9 yields 4, 8, 5. The only element of a that has an absolute 
    difference with each element of b that is always greater than d is 
    element a[2]. Thus the comparator value is 1. 

    Constraints 
    - 1 <= n, m <= 10^5  ; n and m are length or arr1 and arr2
    - 0 <= a[i], b[j], d <= 10^8
"""
from typing import List


def getComparatorVal(a: List[int], b: List[int], d: int) -> int:
    if not a or not b or d < 0:
        return 0

    a.sort()
    b.sort()
    comparator = 0
    for x in a:
        l, r = 0, len(b) - 1
        while l <= r:
            mid = (l + r) // 2
            if abs(b[mid] - x) <= d:
                break
            if x > b[mid]:
                l = mid + 1
            else:
                r = mid - 1
        if l > r:
            comparator += 1
    return comparator


def getComparatorVal_1(a: List[int], b: List[int], d: int) -> int:
    # basic solution O(n^2)
    if not a or not b or d < 0:
        return 0

    cv = 0  # comparator value
    for x in a:
        cc = 0  # current count
        for y in b:
            if abs(x - y) <= d:
                break
            else:
                cc += 1
        if cc == len(b):
            cv += 1

    return cv


assert getComparatorVal([7, 5, 9], [13, 1, 4], 3) == 1
print("Tests Passed!!")

