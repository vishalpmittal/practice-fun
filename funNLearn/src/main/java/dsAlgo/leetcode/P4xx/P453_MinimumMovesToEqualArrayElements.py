"""
    Tag: dp, array, integer

    Given a non-empty integer array of size n, find the minimum number of 
    moves required to make all array elements equal, where a move is 
    incrementing n - 1 elements by 1.

    Example: Input: [1,2,3] Output: 3
    Explanation: Only three moves are needed (remember each move increments two elements):
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
from typing import List
import sys


def minMoves_1(nums: List[int]) -> int:
    # Sort first and then move backwards, find the difference with min and append it to total
    nums.sort()
    count = 0
    for i in range(len(nums)-1, -1, -1):
        count += (nums[i]-nums[0])
    return count


def minMoves_2(nums: List[int]) -> int:
    # DP solution, keep updating nums array with moves so far, use that in next pair calculations
    nums.sort()
    moves = 0
    for i in range(1, len(nums)):
        diff = (moves + nums[i]) - nums[i-1]
        nums[i] += moves
        moves += diff
    return moves


def minMoves_3(nums: List[int]) -> int:
    # (sum of all numbers) - (minimum_number * length of array)
    moves = 0
    min_num = sys.maxsize
    for i in range(0, len(nums)):
        moves += nums[i]
        min_num = min(min_num, nums[i])
    return moves - min_num * len(nums)


def test_code():
    assert minMoves_1([1, 2, 3]) == 3
    assert minMoves_2([1, 2, 3]) == 3
    assert minMoves_3([1, 2, 3]) == 3
    print("Tests Passed!!")


test_code()
