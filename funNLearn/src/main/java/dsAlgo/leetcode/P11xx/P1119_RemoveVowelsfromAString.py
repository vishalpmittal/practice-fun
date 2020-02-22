"""
    Tag: string

    Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' 
    from it, and return the new string.

    Example 1: Input: "leetcodeisacommunityforcoders" Output: "ltcdscmmntyfrcdrs"
    Example 2: Input: "aeiou" Output: ""

    Note:
    S consists of lowercase English letters only.
    1 <= S.length <= 1000
"""
from typing import List


class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join([x for x in S if x not in {'a', 'e', 'i', 'o', 'u'}])


assert Solution().removeVowels('leetcodeisacommunityforcoders') == "ltcdscmmntyfrcdrs"
assert Solution().removeVowels('aeiou') == ''
print('Tests Passed!!')
