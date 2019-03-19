"""
Tag: TO-DO, string, dp, array

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

class P005_LongestPalindromicSubstring(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s


def test_code():
    obj = P005_LongestPalindromicSubstring()
    print "Tests Passed!"

test_code()