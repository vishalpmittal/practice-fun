"""
    Tag: string, array

    Given a list of strings words representing an English Dictionary, find the 
    longest word in words that can be built one character at a time by other 
    words in words. If there is more than one possible answer, return the longest 
    word with the smallest lexicographical order. If there is no answer, return the empty string.

    Example 1: Input:  words = ["w","wo","wor","worl", "world"] Output: "world"
    Explanation: 
    The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    Example 2: Input:  words = ["a", "banana", "app", "appl", "ap", "apply", "apple"] Output: "apple"
    Explanation:  Both "apply" and "apple" can be built from other words in the dictionary. 
    However, "apple" is lexicographically smaller than "apply".

    Note:
    -  All the strings in the input will only contain lowercase letters.
    -  The length of words will be in the range [1, 1000].
    -  The length of words[i] will be in the range [1, 30].
"""

from typing import List


class Solution:
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in xrange(1, len(word))):
                    ans = word

        return ans

    def longestWord_1(self, words):
        def Trie(): return collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans


assert Solution().longestWord(["w", "wo", "wor", "worl", "world"]) == 'world'
assert Solution().longestWord(
    ["a", "banana", "app", "appl", "ap", "apply", "apple"]) == 'apple'
print('Tests Passed!!')
