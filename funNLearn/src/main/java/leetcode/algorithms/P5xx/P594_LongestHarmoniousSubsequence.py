"""
    Tag: dp, array

    We define a harmounious array as an array where the difference between 
    its maximum value and its minimum value is exactly 1.

    Now, given an integer array, you need to find the length of its longest 
    harmonious subsequence among all its possible subsequences.

    Example 1: Input: [1,3,2,2,5,2,3,7]    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 
    Note: The length of the input array will not exceed 20,000.
"""
import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # keep finding the max sum of count[x] and count[x+1]
        # It does not need to be in sequence.
        # As shown in example it can be a non-sequencial sub-set.
        count = collections.Counter(nums)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans


assert Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
print("Tests Passed!!")
