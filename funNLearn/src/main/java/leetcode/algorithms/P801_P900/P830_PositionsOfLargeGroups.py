"""
    Tag: string, array

    In a string S of lowercase letters, these letters form 
    consecutive groups of the same character.

    For example, a string like S = "abbxxxxzyy" has the groups 
    "a", "bb", "xxxx", "z" and "yy".

    Call a group large if it has 3 or more characters.  
    We would like the starting and ending positions of every large group.

    The final answer should be in lexicographic order.

    Example 1: Input: "abbxxxxzzy" Output: [[3,6]]
    Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

    Example 2: Input: "abc" Output: []
    Explanation: We have "a","b" and "c" but no large group.

    Example 3: Input: "abcdddeeeeaabbbcd" Output: [[3,5],[6,9],[12,14]]

    Note:  1 <= S.length <= 1000
"""
from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        i = 0  # The start of each group
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans


assert Solution().largeGroupPositions('abbxxxxzzy') == [[3, 6]]
assert Solution().largeGroupPositions('abc') == []
assert Solution().largeGroupPositions(
    'abcdddeeeeaabbbcd') == [[3, 5], [6, 9], [12, 14]]
print('Tests Passed!!')
