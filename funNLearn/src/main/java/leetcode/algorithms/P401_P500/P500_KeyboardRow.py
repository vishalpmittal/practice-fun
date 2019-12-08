"""
    Tag: string

    Given a List of words, return the words that can be typed using letters of 
    alphabet on only one row's of American keyboard like the image below.

    Example: Input: ["Hello", "Alaska", "Dad", "Peace"]
        Output: ["Alaska", "Dad"]
    
    Note:
    - You may use one character in the keyboard more than once.
    - You may assume the input string will only contain letters of alphabet.
"""
from typing import List


def findWords(words: List[str]) -> List[str]:
    a = set('qwertyuiop')
    b = set('asdfghjkl')
    c = set('zxcvbnm')
    ans = []
    for word in words:
        t = set(word.lower())
        if a & t == t:
            ans.append(word)
        if b & t == t:
            ans.append(word)
        if c & t == t:
            ans.append(word)
    return ans


def test_code():
    assert findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
    print("Tests Passed!!")


test_code()
