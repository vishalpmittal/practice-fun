"""
    Tag: sort
"""
from typing import List


class Solution:
    def insertion_sort(self, A: List[int]) -> List[int]:
        """
            Just like sorting playing cards in our hands
        """

        for i in range(1, len(A)):
            key = A[i]
            j = i - 1

            while j >= 0 and key < A[j]:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key

        return A


assert Solution().insertion_sort([3, 2, 9, 3, 5, 7, 1, 8]) == [1, 2, 3, 3, 5, 7, 8, 9]
print("Tests Passed!")
