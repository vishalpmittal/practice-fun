"""
    Tag: string, array

    Given a text string and words (a list of strings), return all
    index pairs [i, j] so that the substring text[i]...text[j]
    is in the list of words.

    Example 1: Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
    Output: [[3,7],[9,13],[10,17]]

    Example 2: Input: text = "ababa", words = ["aba","ab"]
    Output: [[0,1],[0,2],[2,3],[2,4]]
    Explanation: Notice that matches can overlap, see "aba"
    is found in [0,2] and [2,4].

    Note:
    -  All strings contains only lowercase English letters.
    -  It's guaranteed that all strings in words are different.
    -  1 <= text.length <= 100
    -  1 <= words.length <= 20
    -  1 <= words[i].length <= 50
    -  Return the pairs [i,j] in sorted order (i.e. sort them by their
    first coordinate in case of ties sort them by their second coordinate).
"""
from typing import List


class Solution:
    def indexPairs(self, S: str, words: List[str]) -> List[List[int]]:
        W = set(words)
        return [[i, j-1] for i in range(len(S)) for j in range(len(S)+1) if S[i:j] in W]


assert Solution().indexPairs("thestoryofleetcodeandme", [
    "story", "fleet", "leetcode"]) == [[3, 7], [9, 13], [10, 17]]
assert Solution().indexPairs("ababa", ["aba", "ab"]) == [
    [0, 1], [0, 2], [2, 3], [2, 4]]
assert Solution().indexPairs("baabaaaaaa", ["b", "a", "ba", "bb", "aa"]) == [
    [0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [3, 3], [3, 4], [4, 4], [4, 5], [
        5, 5], [5, 6], [6, 6], [6, 7], [7, 7], [7, 8], [8, 8], [8, 9], [9, 9]
]
print('Tests Passed!!')
