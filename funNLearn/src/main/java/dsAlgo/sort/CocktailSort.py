"""
    Tag: sort
"""
from typing import List


class Solution:
    def cocktail_sort(self, A: List[int]) -> List[int]:
        """
            Variation of bubble sort. 
            Instead of one loop, loop in both the directions
        """
        swapped, start, end = True, 0, len(A) - 1

        while swapped == True:
            swapped = False
            # same as bubble sort
            for i in range(start, end):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    swapped = True

            # if nothing moved, then array is sorted.
            if swapped == False:
                break

            swapped = False
            # end one is in the right spot now
            end = end - 1

            # exactly opposite direction of bubble sort
            for i in range(end - 1, start - 1, -1):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    swapped = True
            # start one is in the right spot now
            start = start + 1
        return A


assert Solution().cocktail_sort([3, 2, 9, 3, 5, 7, 1, 8]) == [1, 2, 3, 3, 5, 7, 8, 9]
print("Tests Passed!")
