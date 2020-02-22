"""
    Tag: string

    Given a string S, return the "reversed" string where all characters 
    that are not a letter stay in the same place, and all letters reverse 
    their positions.

    Example 1: Input: "ab-cd" Output: "dc-ba"
    Example 2: Input: "a-bC-dEf-ghIj" Output: "j-Ih-gfE-dCba"
    Example 3: Input: "Test1ng-Leet=code-Q!" Output: "Qedo1ct-eeLg=ntse-T!"

    Note:
    -  S.length <= 100
    -  33 <= S[i].ASCIIcode <= 122 
    -  S doesn't contain \ or "
"""
from typing import List


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # Stack of Letters
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

    def reverseOnlyLetters_1(self, S: str) -> str:
        # reverse pointer
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)

        return "".join(ans)


assert Solution().reverseOnlyLetters("ab-cd") == "dc-ba"
assert Solution().reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert Solution().reverseOnlyLetters(
    "Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
print('Tests Passed!!')
