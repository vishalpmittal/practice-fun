"""
    tag: array, stack, string

    Given a string s of '(' , ')' and lowercase English characters. 

    Your task is to remove the minimum number of parentheses ( '(' or ')', 
    in any positions ) so that the resulting parentheses string is valid 
    and return any valid string.

    Formally, a parentheses string is valid if and only if:
    - It is the empty string, contains only lowercase characters, or
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.
 
    Example 1: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
    
    Example 2: s = "a)b(c)d"
    Output: "ab(c)d"
    
    Example 3: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.
    
    Example 4: s = "(a(b(c)d)"
    Output: "a(b(c)d)"

    Constraints:
    - 1 <= s.length <= 10^5
    - s[i] is one of  '(' , ')' and lowercase English letters.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
            for every character, 
            if it's a (, put it in stack
            if it's first ), put index in a set
            if it's ) and there's ( in stack for it, don't worry about this pair

            Get the union of indexes of extra lefts from stack and extra right from set
            construct the string and return
        """
        if not s:
            return s

        index_to_remove = set()
        stack = []

        for i, x in enumerate(s):
            if x == "(":
                stack.insert(0, i)
            elif x == ")" and len(stack) == 0:
                index_to_remove.add(i)
            elif x == ")":
                stack.pop()

        for i in stack:
            index_to_remove.add(i)

        ans = ""
        for i, x in enumerate(s):
            if i not in index_to_remove:
                ans += x

        return ans


assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
assert Solution().minRemoveToMakeValid("))((") == ""
assert Solution().minRemoveToMakeValid("(a(b(c)d)") == "(a(bc)d)"
print('Tests Passed!')
