"""
    Tag: array, binary search

    Given a list of sorted characters letters containing only lowercase letters,
    and given a target letter target, find the smallest element in the list that
    is larger than the given target.

    Letters also wrap around. For example, if the target is target = 'z' and
    letters = ['a', 'b'], the answer is 'a'.

    Examples:
    -  Input: letters = ["c", "f", "j"] target = "a" Output: "c"
    -  Input: letters = ["c", "f", "j"] target = "c" Output: "f"
    -  Input: letters = ["c", "f", "j"] target = "d" Output: "f"
    -  Input: letters = ["c", "f", "j"] target = "g" Output: "j"
    -  Input: letters = ["c", "f", "j"] target = "j" Output: "c"
    -  Input: letters = ["c", "f", "j"] target = "k" Output: "c"

    Note:
    -  letters has a length in range [2, 10000].
    -  letters consists of lowercase letters, and contains at least 2 unique letters.
    -  target is a lowercase letter.
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t = ord(target)
        if t < ord(letters[0]) or t >= ord(letters[-1]):
            return letters[0]
        i = 0
        while t >= ord(letters[i]):
            i += 1
        return letters[i]

    def nextGreatestLetter_bs(self, letters: List[str], target: str) -> str:
        # Binary Search approach
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


letters = ["c", "f", "j"]
assert Solution().nextGreatestLetter(letters, "a") == "c"
assert Solution().nextGreatestLetter(letters, "c") == "f"
assert Solution().nextGreatestLetter(letters, "d") == "f"
assert Solution().nextGreatestLetter(letters, "g") == "j"
assert Solution().nextGreatestLetter(letters, "j") == "c"
assert Solution().nextGreatestLetter(letters, "k") == "c"
print('Tests Passed!!')
