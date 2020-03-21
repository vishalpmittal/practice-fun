"""
    Tag: sort
"""
from typing import List


class Solution:
    def partition(self, A: List[int], low: int, high: int) -> int:
        i = low - 1
        pivot = A[high]

        for j in range(low, high):
            if A[j] <= pivot:
                i = i + 1
                A[i], A[j] = A[j], A[i]

        A[i + 1], A[high] = A[high], A[i + 1]
        return i + 1

    def quickSort(self, A: List[int], low: int, high: int):
        """
            -  Pick a pivot, usually the last element in the array. 
            -  start from first element and move the small elements to left and 
            larger elements to right. 
            -  Find the right location for the pivot so that everything on it's 
            left is smaller and everything on it's right is bigger
            -  break the array from pivot. repeat the process for left and right halves. 
        """
        if low < high:
            pi = self.partition(A, low, high)
            self.quickSort(A, low, pi - 1)
            self.quickSort(A, pi + 1, high)

    def QS(self, A: List[int]) -> List[int]:
        self.quickSort(A, 0, len(A) - 1)
        return A


assert Solution().QS([3, 2, 9, 3, 5, 7, 1, 8]) == [1, 2, 3, 3, 5, 7, 8, 9]
print("Tests Passed!")
