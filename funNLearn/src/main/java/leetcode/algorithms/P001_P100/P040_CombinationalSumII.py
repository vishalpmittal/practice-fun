"""
    Tag: integer, math, recursive
    
    Given a collection of candidate numbers (candidates) and a target number (target), 
    find all unique combinations in candidates where the candidate numbers sums to target.

    Each number in candidates may only be used once in the combination.

    Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    
    Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]
    
    Example 2:
    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
        [1,2,2],
        [5]
    ]
"""


class Solution(object):
    @staticmethod
    def combinationSumII(candidates, target):
        candidates.sort()
        return Solution.combinations(candidates, target, [])
    
    @staticmethod
    def combinations(candidates, target, prev_combinations):
        if not target:
            return [prev_combinations]
    
        solutions = []
        for i, num in enumerate(candidates):
            # all solutions include num
            if i > 0 and num == candidates[i-1]:
                continue
            if target >= num:
                solutions.extend(Solution.combinations(
                    candidates[i+1:], target-num, prev_combinations + [num])
                )
            else:
                break
        return solutions

def test_code():
    print Solution.combinationSumII([10,1,2,7,6,1,5], 8)
    print Solution.combinationSumII([2,5,2,1,2], 5)

test_code()
