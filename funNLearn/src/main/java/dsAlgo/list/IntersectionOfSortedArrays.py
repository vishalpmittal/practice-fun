"""
    Tag: arrays

    given two sorted array find the intersection
"""
from typing import List


def find_intersection(a1: List[int], a2: List[int]):
    if not a1 or not a2:
        return []

    # pointer1, pointer2, length1, length2, intersection array
    p1, p2, l1, l2, ia = 0, 0, len(a1), len(a2), []

    while p1 < l1 and p2 < l2:
        if a1[p1] == a2[p2]:
            cv = a1[p1]  # common value
            ia.append(cv)
            while a1[p1] == cv:
                p1 += 1
            while a2[p2] == cv:
                p2 += 1
        elif a1[p1] < a2[p2]:
            p1 += 1
        else:
            p2 += 1

    return ia


assert find_intersection([1, 2, 3, 4, 4, 5], [2, 2, 4, 7, 9]) == [2, 4]
print("tests passed!")
