"""
    Tag: dp, array

    Given an array A of positive integers, A[i] represents the value of 
    the i-th sightseeing spot, and two sightseeing spots i and j have 
    distance j - i between them.

    The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : 
    the sum of the values of the sightseeing spots, minus the distance between them.

    Return the maximum score of a pair of sightseeing spots.

    Example 1: Input: [8,1,5,2,6] Output: 11
    Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
    
    Note:
    -  2 <= A.length <= 50000
    -  1 <= A[i] <= 1000
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        """
            The goal is to keep track of
            Maximum So far and add it to the cur_cell and maintain maximum result
            Here, max_so_far contains : A[i] + i 
            Original Given Formula : A[i] + A[j] + i - j

            Break in two parts : A[i] + i and A[j] -j
            Keep MAX_VALUE of first part among the elements seen so far
            Add the current element to max_so_far and check the result is changing or not
            Also, keep updating the max_so_far at each step
        """
        max_so_far, result = A[0] + 0, 0

        for i in range(1, len(A)):
            result = max(result, max_so_far + A[i] - i)
            max_so_far = max(max_so_far, A[i] + i)

        return result


assert Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
print('Tests Passed!!')
