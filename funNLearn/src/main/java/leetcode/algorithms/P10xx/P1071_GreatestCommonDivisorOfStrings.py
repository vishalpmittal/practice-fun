"""
    Tag: string, math

    For strings S and T, we say "T divides S" if and only if S = T + ... + T  
    (T concatenated with itself 1 or more times)
    Return the largest string X such that X divides str1 and X divides str2.

    Ex1: Ip: str1 = "ABCABC", str2 = "ABC" Output: "ABC"
    Ex2: Ip: str1 = "ABABAB", str2 = "ABAB" Output: "AB"
    Ex3: Ip: str1 = "LEET", str2 = "CODE" Output: ""

    Note:
    -  1 <= str1.length <= 1000
    -  1 <= str2.length <= 1000
    -  str1[i] and str2[i] are English uppercase letters.
"""
from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # imitate gcd algorithm, recursive version.
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
        return True

    def gcdOfStrings_1(self, str1: str, str2: str) -> str:
        # compare substring, iterative version.
        def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))
        return str1[: d] if str1[: d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1 else ''

    def gcdOfStrings_2(self, str1: str, str2: str) -> str:
        # Regular Expression
        def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))
        gcd_str = str1[0: d]
        ptn = '(' + gcd_str + ')+'
        return gcd_str if re.fullmatch(ptn, str1) and re.fullmatch(ptn, str2) else ''


assert Solution().gcdOfStrings("ABCABC", "ABC") == "ABC"
assert Solution().gcdOfStrings("ABABAB", "ABAB") == "AB"
assert Solution().gcdOfStrings("LEET", "CODE") == ""
print('Tests Passed!!')
