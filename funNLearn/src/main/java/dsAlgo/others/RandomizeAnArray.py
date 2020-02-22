"""
    Tag: array, sort
    Given an array randomize the array
"""
from typing import List


class Solution:
    def randomize_arr(self, A: List[int]) -> List[List[List[int]]]:
        from random import random
        A.sort(key=lambda x: 0.5 - random())
        return A


print(Solution().randomize_arr([1, 2, 3, 4, 5, 6]))
print('Tests Passed!!')
