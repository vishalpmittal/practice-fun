"""
    Tag: array, integer

    You have some apples, where arr[i] is the weight of the i-th apple. 
    You also have a basket that can carry up to 5000 units of weight.

    Return the maximum number of apples you can put in the basket.

    Example 1: Input: arr = [100,200,150,1000] Output: 4
    Explanation: All 4 apples can be carried by the basket 
    since their sum of weights is 1450.

    Example 2: Input: arr = [900,950,800,1000,700,800] Output: 5
    Explanation: The sum of weights of the 6 apples 
    exceeds 5000 so we choose any 5 of them.

    Constraints:
    -  1 <= arr.length <= 10^3
    -  1 <= arr[i] <= 10^3
"""
from typing import List


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        summation, cnt = 0, 0
        for number in arr:
            if summation + number < 5000:
                summation += number
                cnt += 1
            else:
                break
        return cnt


assert Solution().maxNumberOfApples([100, 200, 150, 1000]) == 4
assert Solution().maxNumberOfApples([900, 950, 800, 1000, 700, 800]) == 5
print('Tests Passed!!')
