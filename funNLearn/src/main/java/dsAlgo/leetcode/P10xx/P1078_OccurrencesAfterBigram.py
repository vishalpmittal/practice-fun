"""
    Tag: string, array

    Given words first and second, consider occurrences in some text of the
    form "first second third", where second comes immediately after first,
    and third comes immediately after second.
    For each such occurrence, add "third" to the answer, and return the answer.

    Ex1: text = "alice is a good girl she is a good student", first = "a", second = "good"
    Output: ["girl","student"]

    Ex2: text = "we will we will rock you", first = "we", second = "will"
    Output: ["we","rock"]

    Note:
    -  1 <= text.length <= 1000
    -  text consists of space separated words, where each word consists of
    lowercase English letters.
    -  1 <= first.length, second.length <= 10
    -  first and second consist of lowercase English letters.
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        if not text:
            return
        results = []
        text = text.split(" ")
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                results.append(text[i+2])
        return results


assert Solution().findOcurrences("alice is a good girl she is a good student",
                                 "a",  "good") == ["girl", "student"]
assert Solution().findOcurrences(
    "we will we will rock you", "we", "will") == ["we", "rock"]
print('Tests Passed!!')
