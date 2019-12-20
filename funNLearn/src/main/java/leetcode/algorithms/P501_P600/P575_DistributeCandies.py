"""
    Tag: TO-DO, string, dp, array, integer, bit, linked list
    Tag: tree, sort, math, matrix, regex, recursive
    Tag: design ds (design data structure), dfs, binary search, algo

    Given an integer array with even length, where different numbers in this 
    array represent different kinds of candies. Each number means one candy of 
    the corresponding kind. You need to distribute these candies equally in 
    number to brother and sister. Return the maximum number of kinds of candies 
    the sister could gain.

    Example 1: Input: candies = [1,1,2,2,3,3] Output: 3
    Explanation:
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
    The sister has three different kinds of candies. 

    Example 2: Input: candies = [1,1,2,3] Output: 2
    Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
    The sister has two different kinds of candies, the brother has only one kind of candies. 

    Note:
    -  The length of the given array is in range [2, 10,000], and will be even.
    -  The number in given array is in range [-100,000, 100,000].
"""
from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        c_set = set(candies)
        return len(c_set) if len(c_set) < len(candies)/2 else int(len(candies)/2)


assert Solution().distributeCandies([1, 1, 2, 2, 3, 3]) == 3
assert Solution().distributeCandies([1, 1, 2, 3]) == 2
print("Tests Passed!!")