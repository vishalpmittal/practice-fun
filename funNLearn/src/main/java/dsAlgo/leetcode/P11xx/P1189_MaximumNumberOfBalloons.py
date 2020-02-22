"""
    Tag: string

    Given a string text, you want to use the characters of text
    to form as many instances of the word "balloon" as possible.
    You can use each character in text at most once. Return the
    maximum number of instances that can be formed.

    Ex1: I: text = "nlaebolko" Op: 1
    Ex2: I: text = "loonbalxballpoon" Op: 2
    Ex3: I: text = "leetcode" Op: 0

    Constraints:
    -  1 <= text.length <= 10^4
    -  text consists of lower case English letters only.
"""
from typing import List
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        c['l'], c['o'] = c['l'] // 2, c['o'] // 2
        return min([c[i] for i in 'balon'])


assert Solution().maxNumberOfBalloons("nlaebolko") == 1
assert Solution().maxNumberOfBalloons("loonbalxballpoon") == 2
assert Solution().maxNumberOfBalloons("leetcode") == 0
assert Solution().maxNumberOfBalloons("balon") == 0
print('Tests Passed!!')
