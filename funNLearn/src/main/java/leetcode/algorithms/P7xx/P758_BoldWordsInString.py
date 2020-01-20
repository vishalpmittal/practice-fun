"""
    Tag: string, array

    Given a set of keywords words and a string S, make all appearances 
    of all keywords in S bold. Any letters between <b> and </b> tags become bold.

    The returned string should use the least number of tags possible, 
    and of course the tags should form a valid combination.

    For example, given that words = ["ab", "bc"] and S = "aabcd", we 
    should return "a<b>abc</b>d". 
    Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

    Note:
    -  words has length in range [0, 50].
    -  words[i] has length in range [1, 10].
    -  S has length in range [0, 500].
    -  All characters in words[i] and S are lowercase letters.
"""
from typing import List
import re


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        # words = ["ab", "bc"], S = "aabcd"
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i+len(word), N)):
                        mask[j] = True

        # mask = [False, True, True, True, False]
        NS, bold = '', False
        for i, m in enumerate(mask):
            if m and not bold:
                NS += '<b>'
                bold = True
            elif not m and bold:
                NS += '</b>'
                bold = False
            NS += S[i]

        if bold:
            NS += '</b>'
        return NS


assert Solution().boldWords(["ab", "bc"], "a<b>abc</b>d")
assert Solution().boldWords(["ab", "bc", "cd"], "a<b>abcd</b>")
print('Tests Passed!!')
