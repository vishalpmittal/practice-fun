"""
    Tag: string, math

    Given a non-empty string check if it can be constructed by taking a substring of 
    it and appending multiple copies of the substring together. You may assume the given 
    string consists of lowercase English letters only and its length will not exceed 10000.

    Example 1: Input: "abab"  Output: True
    Explanation: It's the substring "ab" twice.

    Example 2: Input: "aba" Output: False

    Example 3: Input: "abcabcabcabc"  Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

'''
    Brilliant Solution by mrjerryho in leetcode

    To find if the string has a repeatable substring inside, we can create a new 
    string by duplicating the original string.
    Ex. "abcabc" => "abcabcabcabc"
    By removing the first and last character of the new string we create the string "bcabcabcabcab"
    If the original string "abcabc" is in "bcabcabcab", we return true.

    Why it works:
    If the original string has a repeating substring, the repeating substring can be no 
    larger than 1/2 the length of the original string. I.e "xyxy" would be "xy"
    By repeating the string and removing the first and last character of the new string, 
    I.e "xyxyxyxy" => "yxyxyx", if the original string "xyxy" can be found in "yxyxyx", it 
    means that "xyxy" has a repeating substring.

    However, this solution doesn't tell us what the repeating substring is, but does 
    solve the question if it exists.
'''
def repeatedSubstringPattern(self, s: str) -> bool:
    return s in (s+s)[1:-1]

def repeatedSubstringPattern_1(s: str) -> bool:
    """
    -  The length of the repeating substring must be a divisor of the length of 
       the input string
    -  Search for all possible divisor of str.length, starting for length/2
    -  If i is a divisor of length, repeat the substring from 0 to i the number of 
       times i is contained in s.length
    -  If the repeated substring is equals to the input str return true
    """
    if not s or len(s) < 2:
        return False

    s_len = len(s)
    for i in range(int(s_len/2), 0, -1):
        if (s_len % i == 0):
            temp_str = ''
            for j in range(0,  int(s_len / i)):
                temp_str += s[0:i]
            if temp_str == s:
                return True
    return False

def test_code():
    assert repeatedSubstringPattern_1('abab') == True
    assert repeatedSubstringPattern_1('aba') == False
    assert repeatedSubstringPattern_1('abcabcabcabc') == True
    print ("Tests Passed!!")

test_code()
