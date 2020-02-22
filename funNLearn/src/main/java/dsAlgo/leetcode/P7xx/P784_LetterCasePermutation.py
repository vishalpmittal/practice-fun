"""
    Tag: string, dp, array

    Given a string S, we can transform every letter individually to be lowercase 
    or uppercase to create another string.  
    Return a list of all possible strings we could create.

    Examples: 
    -  Input: S = "a1b2" Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
    -  Input: S = "3z4" Output: ["3z4", "3Z4"]
    -  Input: S = "12345" Output: ["12345"]

    Note:
    -  S will be a string with length between 1 and 12.
    -  S will consist only of letters or digits.
"""
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [S]
        for i in range(len(S)):
            if not S[i].isalpha():
                continue
            r = S[i].upper() if S[i].islower() else S[i].lower()
            ans.extend([w[:i] + r + w[i + 1:] for w in ans.copy()])

        return ans


assert Solution().letterCasePermutation('a1b2') == [
    'a1b2', 'A1b2', 'a1B2', 'A1B2']
assert Solution().letterCasePermutation('3z4') == ["3z4", "3Z4"]
assert Solution().letterCasePermutation('12345') == ["12345"]
assert Solution().letterCasePermutation('C') == ['C', 'c']
assert Solution().letterCasePermutation("Jw") == ['Jw', 'jw', 'JW', 'jW']

print('Tests Passed!!')
