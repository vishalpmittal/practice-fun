"""
    Tag: array, integer

    Given an array of distinct integers arr, find all pairs 
    of elements with the minimum absolute difference of any two elements. 
    Return a list of pairs in ascending order(with respect to pairs), 
    each pair [a, b] follows

    -  a, b are from arr
    -  a < b
    -  b - a equals to the minimum absolute difference of any 
    two elements in arr
    
    Example 1: Input: arr = [4,2,1,3] Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. 
    List all pairs with difference equal to 1 in ascending order.

    Example 2: Input: arr = [1,3,6,10,15] Output: [[1,3]]
    Example 3: Input: arr = [3,8,-10,23,19,-4,-14,27] 
    Output: [[-14,-10],[19,23],[23,27]]

    Constraints:
    -  2 <= arr.length <= 10^5
    -  -10^6 <= arr[i] <= 10^6
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort()
        ans, diff = [], float('inf')
        for i in range(1, len(a)):
            if diff >= a[i] - a[i - 1]:
                if diff > a[i] - a[i - 1]:
                    # ans.clear()           # modified to the follow to achieve O(1) time, credit to @vivek_23.
                    ans = []
                    diff = a[i] - a[i - 1]
                ans.append([a[i - 1], a[i]])
        return ans

    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort()
        diff = min(a[i] - a[i - 1] for i in range(1, len(a)))
        return [[a[i - 1], a[i]] for i in range(1, len(a)) if a[i] - a[i - 1] == diff]


assert Solution().minimumAbsDifference(
    [4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]
assert Solution().minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]]
assert Solution().minimumAbsDifference(
    [3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]]
print('Tests Passed!!')
