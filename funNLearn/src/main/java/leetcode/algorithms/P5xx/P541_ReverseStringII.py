"""
    Tag: string, array

    Given a string and an integer k, you need to reverse the first k 
    characters for every 2k characters counting from the start of the string. 
    If there are less than k characters left, reverse all of them. If there are 
    less than 2k but greater than or equal to k characters, then reverse the first k 
    characters and left the other as original.

    Example:  Input: s = "abcdefg", k = 2   Output: "bacdfeg"

    Restrictions:
    -  The string consists of lower English letters only.
    -  Length of the given string and k will in the range [1, 10000]
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return s

        ls = list(s)
        rev, i = True, 0
        while i < len(ls):
            if rev:
                j = min(i + k-1, len(ls)-1)
                while i < j:
                    ls[i], ls[j] = ls[j], ls[i]  # swap
                    i += 1
                    j -= 1
            i += 1
            if i % k == 0 and (i/k) % 2 == 0:
                rev = True
            else:
                rev = False

        return ''.join(ls)

    def reverseStr_1(self, s, k):
        # Use python's way to reverse
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)


assert Solution().reverseStr('abcdefgh', 3) == 'cbadefhg'
assert Solution().reverseStr('abcdefghij', 3) == 'cbadefihgj'
assert Solution().reverseStr_1('abcdefgh', 3) == 'cbadefhg'
assert Solution().reverseStr_1('abcdefghij', 3) == 'cbadefihgj'
print('Tests Passed!')
