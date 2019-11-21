"""
    Tag: array
    
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some 
    elements appear twice and others appear once.

    Find all the elements of [1, n] inclusive that do not appear in this array.

    Could you do it without extra space and in O(n) runtime? 
    You may assume the returned list does not count as extra space.

    Example: Input: [4,3,2,7,8,2,3,1]
    Output: [5,6]
"""
from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    num_set = set()
    ret_list = []

    max_num = -1
    for n in nums:
        num_set.add(n)
        max_num = max(max_num, n)

    for x in range(1, max_num):
        if x not in num_set:
            ret_list.append(x)
    return ret_list


def findDisappearedNumbers_1(nums: List[int]) -> List[int]:
    if not nums or len(nums) == 0:
        return []

    num_set = set(range(1, len(nums)+1))
    for n in nums:
        num_set.discard(n)
    return list(num_set)


def findDisappearedNumbers_2(nums: List[int]) -> List[int]:
    if not nums or len(nums) == 0:
        return []
    
    res = set()
    for n in nums:
        while nums[n-1] != n:
            tmp = nums[n-1]
            nums[n-1] = n
            n = tmp

    for i in range(1, len(nums)):
        if nums[i] != i+1: res.add(i+1)
    return list(res)


def test_code():
    assert findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert findDisappearedNumbers_1([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert findDisappearedNumbers_2([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    print("Tests Passed!!")


test_code()
