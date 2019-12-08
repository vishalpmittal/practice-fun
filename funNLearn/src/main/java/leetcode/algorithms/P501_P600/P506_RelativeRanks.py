"""
    Tag: array

    Given scores of N athletes, find their relative ranks and the people with 
    the top three highest scores, who will be awarded medals: 
    "Gold Medal", "Silver Medal" and "Bronze Medal".

    Example 1:
    Input: [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    Explanation: The first three athletes got the top three highest scores, 
    so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
    For the left two athletes, you just need to output their relative 
    ranks according to their scores.

    Note:
    - N is a positive integer and won't exceed 10,000.
    - All the scores of athletes are guaranteed to be unique.
"""
from typing import List


def findRelativeRanks(nums: List[int]) -> List[str]:
    pos = {}
    for i in range(0, len(nums)):
        pos[nums[i]] = i
    sorted_nums = sorted(pos, reverse=True)
    for j in range(0, len(sorted_nums)):
        if j == 0:
            nums[pos[sorted_nums[j]]] = 'Gold Medal'
        elif j == 1:
            nums[pos[sorted_nums[j]]] = 'Silver Medal'
        elif j == 2:
            nums[pos[sorted_nums[j]]] = 'Bronze Medal'
        else:
            nums[pos[sorted_nums[j]]] = str(j+1)
    return nums


def test_code():
    assert findRelativeRanks([4, 5, 2, 3, 1]) == [
        'Silver Medal', 'Gold Medal', 4, 'Bronze Medal', 5]
    print("Tests Passed!!")


test_code()
