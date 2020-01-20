"""
    Tag: integer, math, recursive
    
    Given a set of candidate numbers (candidates) (without duplicates) and a 
    target number (target), find all unique combinations in candidates where 
    the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

    Example 1:
    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]

    Example 2:
    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]
"""


class Solution(object):
    @staticmethod
    def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []

        def helper(candidates, target, t):
            print('(candidates: {}, target: {}, t: {})'.format(candidates, target, t))
            if not target:
                ans.append(t)
                return
            for i, num in enumerate(candidates):
                print('i: {}, num: {}'.format(i, num))
                if target >= num:
                    helper(candidates[i:], target - num, t + [num])
                else: break

        helper(candidates, target, [])
        return ans

def test_code():
    print Solution.combinationSum([2,3,5], 8)

test_code()
