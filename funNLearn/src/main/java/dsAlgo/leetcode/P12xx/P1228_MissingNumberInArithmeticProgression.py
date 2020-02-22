"""
    Tag: array, integer, binary search

    In some array arr, the values were in arithmetic progression:
    the values arr[i+1] - arr[i] are all equal for
    every 0 <= i < arr.length - 1.
    Then, a value from arr was removed that was not the first or
    last value in the array. Return the removed value.

    Example 1: Input: arr = [5,7,11,13] Output: 9
    Explanation: The previous array was [5,7,9,11,13].

    Example 2: Input: arr = [15,13,12] Output: 14
    Explanation: The previous array was [15,14,13,12].

    Constraints:
    3 <= arr.length <= 1000
    0 <= arr[i] <= 10^5
    """
from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        md = float('inf')
        for i in range(len(arr)-1):
            cd = arr[i]-arr[i+1]
            if abs(md) > abs(cd):
                md = cd
            elif cd == md:
                break

        for i in range(len(arr)-1):
            if arr[i]-arr[i+1] != md:
                return arr[i] - md
        return arr[-1] + md

    def missingNumber_formula(self, A: List[int]) -> int:
        """
            arithmetic sequence sum = (first + last) * n / 2
            In this problem, the first and last value are not removed.
            first = min(A), last = max(A)
            We can calulate the sum of arithmetic sequence.
            The difference between sum - sum(A) is the missing number.
        """
        return (min(A) + max(A)) * (len(A) + 1) / 2 - sum(A)

    def missingNumber_binarySearch(self, A: List[int]) -> int:
        # Binary Search O(log n)
        # Assumption : the first and last value are not removed
        n = len(A)
        d = (A[-1] - A[0]) / n
        left, right = 0, n
        while left < right:
            mid = (left + right) / 2
            if A[mid] == A[0] + d * mid:
                left = mid + 1
            else:
                right = mid
        return A[0] + d * left


assert Solution().missingNumber([5, 7, 11, 13]) == 9
assert Solution().missingNumber([15, 13, 12]) == 14
assert Solution().missingNumber([100, 300, 400]) == 200
print('Tests Passed!!')
