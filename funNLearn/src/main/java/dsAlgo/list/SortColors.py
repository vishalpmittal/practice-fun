"""
    tag: list, sort

    Given an array of n objects with 2 different colors (numbered from 1, 2 ), 
    sort them so that objects of the same color are adjacent 

    [1,2,1,2,1,1] -> [1,1,1,1,2,2]

    Further:
    --------
    Given an array of n objects with 3 different colors (numbered from 1, 2, 3 ), 
    sort them so that objects of the same color are adjacent . in ascending order

    [1, 2, 3, 3, 1, 3, 2, 1, 1] -> [1, 1, 1, 1, 2, 2, 3, 3, 3]
"""
from typing import List


def sort_2_colors(CL: List[int]):
    if not CL or len(CL) < 2:
        return

    i, j = 0, len(CL) - 1
    while i < j:
        while CL[i] == 1:
            i += 1
        while CL[j] == 2:
            j -= 1
        if i < j:
            CL[i], CL[j] = 1, 2


def sort_3_colors(CL: List[int]):
    if not CL or len(CL) < 3:
        return

    i, j, k = 0, 0, len(CL) - 1
    while i <= j < k:
        _min_ = min(CL[i], CL[j], CL[k])
        _max_ = max(CL[i], CL[j], CL[k])
        _mid_ = CL[i] + CL[j] + CL[k] - _min_ - _max_
        CL[i], CL[j], CL[k] = _min_, _mid_, _max_

        while CL[i] == 1:
            if j == i:
                j += 1
            i += 1

        while CL[j] == 2:
            j += 1

        while CL[k] == 3:
            k -= 1


col_list = [1, 2, 1, 2, 1, 1]
sort_2_colors(col_list)
assert col_list == [1, 1, 1, 1, 2, 2]

col_list = [1, 2, 3, 3, 1, 3, 2, 1, 1]
sort_3_colors(col_list)
assert col_list == [1, 1, 1, 1, 2, 2, 3, 3, 3]

print("Tests passed!")
