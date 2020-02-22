"""
    Tag: string

    Implement function ToLowerCase() that has a string parameter str, 
    and returns the same string in lowercase.

    Example 1: Input: "Hello" Output: "hello"
    Example 2: Input: "here" Output: "here"
    Example 3: Input: "LOVELY" Output: "lovely"
"""
from typing import List


class Solution:
    def toLowerCase(self, str: str) -> str:
        L = list(str)
        for i in range(len(L)):
            if 64 < ord(L[i]) < 97:
                L[i] = chr(ord(L[i])+32)
            else:
                continue
        return "".join(L)


assert Solution().toLowerCase('Hello') == 'hello'
assert Solution().toLowerCase('here') == 'here'
assert Solution().toLowerCase('LOVELY') == 'lovely'
print('Tests Passed!!')
