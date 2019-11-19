"""
    Tag: string, dp, stack

    Given a string containing just the characters '(' and ')', find the 
    length of the longest valid (well-formed) parentheses substring.

    Example 1:
    Input: "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()"

    Example 2:
    Input: ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()"
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0
        
        for c in s:
            # print (c: {}, stack {}, longest: {}'.format(c, stack, longest))
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest

def test_code():
    obj = Solution()
    assert obj.longestValidParentheses('(()') == 2
    assert obj.longestValidParentheses(')()())') == 4
    assert obj.longestValidParentheses('()(()') == 2
    assert obj.longestValidParentheses('()())((((((()))))))') == 14
    print ("Tests Passed!")

test_code()
