"""
    Tag: string, regex, recursive

    Given an input string (s) and a pattern (p), implement regular expression matching 
    with support for '.' and '*'.

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).

    Note:
    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

    Example 1: Input: s = "aa" p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

    Example 2: Input: s = "aa" p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. 
                Therefore, by repeating 'a' once, it becomes "aa".

    Example 3: Input: s = "ab" p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

    Example 4: Input: s = "aab" p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

    Example 5: Input: s = "mississippi" p = "mis*is*p*."
    Output: false
"""

class P010_RegularExpressionMatching(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return s is ''

        # Just a basic check of first char
        firstMatch = len(s) > 0 and (s[0] == p[0] or p[0] == '.')

        # if p has a * at current+1 location
        if len(p) >=2 and p[1] == '*':
            # s, p[2:] = zero char matches
            # s[1:, p] = 1 or more match
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:
            # no star found match the remaining string
            return firstMatch and self.isMatch(s[1:], p[1:])

def test_code():
    obj = P010_RegularExpressionMatching()
    assert(obj.isMatch('aa', 'a') == False)
    assert(obj.isMatch('aa', 'a*') == True)
    assert(obj.isMatch('ab', '.*') == True)
    assert(obj.isMatch('aab', 'c*a*b') == True)
    assert(obj.isMatch('mississippi', 'mis*is*p*.') == False)
    assert(obj.isMatch('abadlfkadfkd', '.*') == True)
    print ("Tests Passed!")

test_code()