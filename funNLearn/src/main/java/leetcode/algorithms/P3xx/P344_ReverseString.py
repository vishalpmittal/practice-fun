"""
    Tag: string, array
    
    Write a function that reverses a string. The input string is given as an array of characters char[].
    Do not allocate extra space for another array, you must do this by modifying the 
    input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.
    
    Example 1: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    
    Example 2: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, int(len(s)/2)):
            tmp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = tmp

def test_code():
    s = ['a', 'b', 'c']
    Solution().reverseString(s)
    assert s == ['c', 'b', 'a']
    print ("Tests Passed!!")

test_code()
