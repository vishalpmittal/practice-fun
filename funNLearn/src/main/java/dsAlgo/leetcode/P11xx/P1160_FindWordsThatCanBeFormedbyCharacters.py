"""
    Tag: string

    You are given an array of strings words and a string chars.
    A string is good if it can be formed by characters from
    chars (each character can only be used once).
    Return the sum of lengths of all good strings in words.

    Ex1: I: words = ["cat","bt","hat","tree"], chars = "atach" ; O: 6
    Explanation:
    The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

    Ex2: I: words = ["hello","world","leetcode"], chars = "welldonehoneyr" ; O: 10
    Explanation:
    The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

    Note:
    -  1 <= words.length <= 1000
    -  1 <= words[i].length, chars.length <= 100
    -  All strings contain lowercase English letters only.
"""
from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum, chars_counter = 0, collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                sum += len(word)
        return sum


assert Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6
assert Solution().countCharacters(
    ["hello", "world", "leetcode"], "welldonehoneyr") == 10
print('Tests Passed!!')
