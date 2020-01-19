"""
    Tag: math

    A decimal number can be converted to its Hexspeak representation 
    by first converting it to an uppercase hexadecimal string, then 
    replacing all occurrences of the digit 0 with the letter O, and the 
    digit 1 with the letter I.  Such a representation is valid if and 
    only if it consists only of the letters in the 
    set {"A", "B", "C", "D", "E", "F", "I", "O"}.

    Given a string num representing a decimal integer N, return the 
    Hexspeak representation of N if it is valid, otherwise return "ERROR".

    Example 1: Input: num = "257" Output: "IOI"
    Explanation:  257 is 101 in hexadecimal.

    Example 2: Input: num = "3" Output: "ERROR"

    Constraints:
    -  1 <= N <= 10^12
    -  There are no leading zeros in the given string.
    -  All answers must be in uppercase letters.
"""
from typing import List


class Solution:
    def toHexspeak_0(self, num: str) -> str:
        ha = ['O', 'I', '2', '3', '4', '5', '6', '7',
              '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        num = int(num)
        hn, num = ha[num % 16], num // 16
        while num > 0:
            hn, num = ha[num % 16] + hn, num // 16
        return hn if all(x in {'A', 'B', 'C', 'D', 'E', 'F', 'O', 'I'} for x in hn) else 'ERROR'

    def toHexspeak(self, num: str) -> str:
        hn = str(hex(int(num)))[2:].upper().replace('1', 'I').replace('0', 'O')
        return hn if all(x in {'A', 'B', 'C', 'D', 'E', 'F', 'O', 'I'} for x in hn) else 'ERROR'


assert Solution().toHexspeak('257') == 'IOI'
assert Solution().toHexspeak('3') == 'ERROR'
assert Solution().toHexspeak("747823223228") == "AEIDBCDIBC"
print('Tests Passed!!')
