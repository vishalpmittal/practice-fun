"""
    Tag: array

    Suppose Andy and Doris want to choose a restaurant for dinner, and 
    they both have a list of favorite restaurants represented by strings.

    You need to help them find out their common interest with the least list index sum. 
    If there is a choice tie between answers, output all of them with no order 
    requirement. You could assume there always exists an answer.

    Example 1:  Input: ["Shogun", "Tapioca Express", "Burger King", "KFC"]
                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
                Output: ["Shogun"]
                Explanation: The only restaurant they both like is "Shogun".

    Example 2:  Input: ["Shogun", "Tapioca Express", "Burger King", "KFC"]
                ["KFC", "Shogun", "Burger King"]
                Output: ["Shogun"]
                Explanation: The restaurant they both like and have the least index 
                sum is "Shogun" with index sum 1 (0+1).

    Note:
    -  The length of both lists will be in the range of [1, 1000].
    -  The length of strings in both lists will be in the range of [1, 30].
    -  The index is starting from 0 to the list length minus 1.
    -  No duplicates in both lists.
"""

from typing import List


class Solution:
    def solve_problem(self, l1: List[str], l2: List[str]) -> List[str]:
        l1_seq = {r1: i1 for i1, r1 in enumerate(l1)}
        indx_sum, rests = 1e9, []

        for i2, r2 in enumerate(l2):
            i1 = l1_seq.get(r2, 1e9)
            if i1 + i2 < indx_sum:
                indx_sum = i1 + i2
                rests = [r2]
            elif i1 + i2 == indx_sum:
                rests.append(r2)
        return rests


assert Solution().solve_problem(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"]
assert Solution().solve_problem(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                ["KFC", "Shogun", "Burger King"]) == ["Shogun"]
print('Tests Passed!!')
