"""
    Tag: sort
"""
from typing import List


class Solution:
    def merge_sort(self, A: List[int]) -> List[int]:
        """
            divide and conquer algorithm. divide the array in two halvess and 
            sort the two halves while merging.
        """
        if len(A) > 1:
            mid = len(A) // 2
            L, R = A[:mid], A[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                A[k] = L[i]
                i, k = i + 1, k + 1

            while j < len(R):
                A[k] = R[j]
                j, k = j + 1, k + 1


arr = [3, 2, 9, 3, 5, 7, 1, 8]
Solution().merge_sort(arr)
assert arr == [1, 2, 3, 3, 5, 7, 8, 9]
print("Tests Passed!")
