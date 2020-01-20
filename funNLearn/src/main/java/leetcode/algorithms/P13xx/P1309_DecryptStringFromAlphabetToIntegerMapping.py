"""
    Tag: string, array

    Given a string s formed by digits ('0' - '9') and '#' . We want to 
    map s to English lowercase characters as follows:
    -  Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    -  Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 

    Return the string formed after mapping.
    It's guaranteed that a unique mapping will always exist.

    Example 1: Input: s = "10#11#12" Output: "jkab"
    Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

    Example 2: Input: s = "1326#" Output: "acz"
    Example 3: Input: s = "25#" Output: "y"
    Example 4: Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    Output: "abcdefghijklmnopqrstuvwxyz"

    Constraints:
    -  1 <= s.length <= 1000
    -  s[i] only contains digits letters ('0'-'9') and '#' letter.
    -  s will be valid string such that mapping is always possible.
"""
from typing import List


class Solution:

    def freqAlphabets(self, s: str) -> str:
        i, ans = 0, ''
        while i < len(s)-2:
            increm = 2 if s[i+2] == '#' else 1
            ans += chr(int(s[i:i+increm]) + 96)
            i = i + 1 if increm == 1 else i+increm+1
        while i < len(s):
            ans += chr(int(s[i]) + 96)
            i += 1
        return ans

    def freqAlphabets_1(self, s: str) -> str:
        # Great hack with i> 9
        for i in range(26, 0, -1):
            s = s.replace(str(i)+'#'*(i > 9), chr(96+i))
        return s


assert Solution().freqAlphabets("10#11#12") == "jkab"
assert Solution().freqAlphabets("1326#") == "acz"
assert Solution().freqAlphabets("25#") == "y"
assert Solution().freqAlphabets(
    "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#") == "abcdefghijklmnopqrstuvwxyz"


print('Tests Passed!!')
