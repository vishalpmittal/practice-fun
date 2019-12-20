"""
    Tag: math, matrix

    Given an array with n integers, your task is to check if it could 
    become non-decreasing by modifying at most 1 element.

    We define an array is non-decreasing if array[i] <= array[i + 1] holds
    for every i (1 <= i < n).

    Example 1:  Input: [4,2,3]  Output: True
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

    Example 2:  Input: [4,2,1]  Output: False
    Explanation: You can't get a non-decreasing array by modify at most one element.

    Note: The n belongs to [1, 10,000]
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        '''
            The logic is to first find any inversions, and if the number of inversions 
            is > 1, then we need to modify more than 1 element and hence we return False.
            Once we find an inversion,
            We have to fix either the current value or the next value appropriately so 
            that any future inversions can be detected correctly.
        '''
        count_dec = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count_dec += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
            if count_dec > 1:
                return False
        return True


assert Solution().checkPossibility([4, 2, 3])
assert not Solution().checkPossibility([4, 2, 1])
print('Tests Passed!!')
