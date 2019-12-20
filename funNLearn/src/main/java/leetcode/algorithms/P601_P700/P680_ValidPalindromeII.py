"""
    Tag: TO-DO, string, dp, array, integer, bit, linked list
    Tag: tree, sort, math, matrix, regex, recursive
    Tag: design ds (design data structure), dfs, binary search, algo

    Given a non-empty string s, you may delete at most one character. 
    Judge whether you can make it a palindrome.

    Example 1:   Input: "aba"   Output: True

    Example 2:   Input: "abca"  Output: True
    Explanation: You could delete the character 'c'.

    Note:
    -  The string will only contain lowercase characters a-z. 
    -  The maximum length of the string is 50000.
"""
from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
            For each index i in the given string, let's remove that character, 
            then check if the resulting string is a palindrome. If it is, 
            (or if the original string was a palindrome), then we'll return true
        '''
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]:
                return True
        return s == s[::-1]

    def validPalindrome_1(self, s):
        '''
            Suppose we want to know whether s[i], s[i+1], ..., s[j] form a 
            palindrome. If i >= j then we are done. If s[i] == s[j] then we may 
            take i++; j--. Otherwise, the palindrome must be either 
            s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should 
            check both cases.
        '''
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) / 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True


assert Solution().validPalindrome("ebcbbececabbacecbbcbe")
assert Solution().validPalindrome("aba")
assert Solution().validPalindrome("abca")
assert not Solution().validPalindrome("abc")
print('Tests Passed!!')
