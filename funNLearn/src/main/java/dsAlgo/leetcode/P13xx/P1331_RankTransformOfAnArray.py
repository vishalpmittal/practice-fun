"""
    Tag: array

    Given an array of integers arr, replace each element with its rank.
    The rank represents how large the element is. The rank has the following rules:

    - Rank is an integer starting from 1.
    - The larger the element, the larger the rank. 
      If two elements are equal, their rank must be the same.
    - Rank should be as small as possible.
 
    Example 1: [40,10,20,30]
    Output: [4,1,2,3]
    Explanation: 
    40 is the largest element. 
    10 is the smallest. 20 is the second smallest. 30 is the third smallest.

    Example 2: [100,100,100]
    Output: [1,1,1]
    Explanation: Same elements share the same rank.
    
    Example 3: arr = [37,12,28,9,100,56,80,5,12]
    Output: [5,3,4,2,8,6,7,1,3]

    Constraints:
    -  0 <= arr.length <= 105
    -  -109 <= arr[i] <= 109
"""
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_2_positions = {}
        for pos, n in enumerate(arr):
            num_2_positions[n] = num_2_positions.get(n, list())
            num_2_positions[n].append(pos)

        rank = 1
        for num in sorted(num_2_positions.keys()):
            for pos in num_2_positions[num]:
                arr[pos] = rank
            rank += 1

        return arr
        
    def arrayRankTransform_swag(self, arr: List[int]) -> List[int]:
        d = dict((n, i+1) for i, n in enumerate(sorted(set(arr))))
        return [d[x] for x in arr]

    def test(self):
        assert self.arrayRankTransform([100,100,100]) == [1,1,1]
        assert self.arrayRankTransform([37,12,28,9,100,56,80,5,12]) == [5,3,4,2,8,6,7,1,3]
        assert self.arrayRankTransform([40,10,20,30]) == [4,1,2,3]
        print('Tests Passed!')

Solution().test()