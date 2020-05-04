"""
    tag: dp, string

    Given two strings text1 and text2, return the length of their longest common subsequence.

    A subsequence of a string is a new string generated from the original string with 
    some characters(can be none) deleted without changing the relative order of the 
    remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
    A common subsequence of two strings is a subsequence that is common to both strings.

    If there is no common subsequence, return 0.
    
    Example 1: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.

    Example 2: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.
    
    Example 3:text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.
 
    Constraints:
    - 1 <= text1.length <= 1000
    - 1 <= text2.length <= 1000
    - The input strings consist of lowercase English characters only.
"""
from typing import List


class Solution:
    def longestCommonSubsequence(self, S1: str, S2: str) -> int:
        """
            dp logic: for i,j if s1[j] is not equal to s2[i]
            take the max of previous top or left element
            else if chars are equal take the diagonal value +1

                   a  b  c  d  e
              [[0, 0, 0, 0, 0, 0 ],                    
            a  [0, 1, 1, 1, 1, 1 ], 
            c  [0, 1, 1, 2, 2, 2 ], 
            e  [0, 1, 1, 2, 2, 3 ]] 

        """
        dp = [[0 for _ in range(len(S1) + 1)] for _ in range(len(S2) + 1)]
        for i in range(1, len(S2) + 1):
            for j in range(1, len(S1) + 1):
                if S2[i - 1] == S1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[-1][-1]


print(Solution().longestCommonSubsequence("abcd", "aabbccdd"))
