"""
    Tag: string

    Your friend is typing his name into a keyboard.  
    Sometimes, when typing a character c, the key might get 
    long pressed, and the character will be typed 1 or more times.

    You examine the typed characters of the keyboard.  
    Return True if it is possible that it was your friends name, 
    with some characters (possibly none) being long pressed.

    Example 1: Input: name = "alex", typed = "aaleex"  Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.

    Example 2: Input: name = "saeed", typed = "ssaaedd" Output: false
    Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

    Example 3: Input: name = "leelee", typed = "lleeelee" Output: true

    Example 4: Input: name = "laiden", typed = "laiden" Output: true
    Explanation: It's not necessary to long press any character.
    
    Note:
    -  name.length <= 1000
    -  typed.length <= 1000
    -  The characters of name and typed are lowercase letters.
"""
from typing import List


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, t = 0, 0
        while n < len(name) and t < len(typed):
            if typed[t] == name[n]:
                t += 1
                n += 1
            elif n > 0 and typed[t] == name[n-1]:
                t += 1
            else:
                return False
        if t < len(typed):
            return all(name[n-1] == x for x in typed[t:])
        return n == len(name) and t == len(typed)


assert Solution().isLongPressedName("alex", "aaleex")
assert not Solution().isLongPressedName("saeed", "ssaaedd")
assert Solution().isLongPressedName("leelee", "lleeelee")
assert Solution().isLongPressedName("laiden", "laiden")
assert not Solution().isLongPressedName("pyplrz", "ppyypllr")
assert Solution().isLongPressedName("vtkgn", "vttkgnn")
print('Tests Passed!!')
