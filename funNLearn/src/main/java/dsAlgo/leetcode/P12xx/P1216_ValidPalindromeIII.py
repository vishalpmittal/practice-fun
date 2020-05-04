"""
    tag: string

    Given a string s and an integer k, find out if the given string 
    is a K-Palindrome or not.

    A string is K-Palindrome if it can be transformed into a palindrome 
    by removing at most k characters from it.

    Example 1: s = "abcdeca", k = 2
    Output: true
    Explanation: Remove 'b' and 'e' characters.
 
    Constraints:
    - 1 <= s.length <= 1000
    - s has only lowercase English letters.
    - 1 <= k <= s.length
"""
from typing import List


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
            A palindrome is same forward and backwards
            - Find out the length of longest common subsequence of the string and it's reverse
            - return len(s) - lcs <= k

            Look P1143_LongestCommonSubsequence for DP explaination of LCS finding
        """
        if len(s) < 2 and k >= 0:
            return True

        S1, S2 = s, s[::-1]
        dp = [[0 for _ in range(len(S1) + 1)] for _ in range(len(S2) + 1)]
        for i in range(1, len(S2) + 1):
            for j in range(1, len(S1) + 1):
                if S2[i - 1] == S1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return len(s) - dp[-1][-1] <= k


assert Solution().isValidPalindrome(s="abcdeca", k=2)
print("Tests Passed!")
