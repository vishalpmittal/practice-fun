"""
    Tag: array, bit

    Given a binary array, find the maximum number of consecutive 1s in this array.

    Example 1: Input: [1,1,0,1,1,1], Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

    Note:
    1. The input array will only contain 0 and 1.
    2. The length of input array is a positive integer and will not exceed 10,000
"""
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    if not nums:
        return 0
    max_cons = -1
    curr_count = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            curr_count += 1
        else:
            max_cons = max(max_cons, curr_count)
            curr_count = 0
        max_cons = max(max_cons, curr_count)
    return max_cons


def test_code():
    assert findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    print("Tests Passed!!")


test_code()
