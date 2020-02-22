"""
    Tag: string

    Given a string, you need to reverse the order of characters in 
    each word within a sentence while still preserving whitespace and 
    initial word order.

    Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    
    Note: In the string, each word is separated by single space and there 
    will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # default spit is on space
        return ' '.join([x[::-1] for x in s.split()])


assert Solution().reverseWords(
    "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
print("Tests Passed!!")
