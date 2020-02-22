"""
    Tag: string, math

    Given a word, you need to judge whether the usage of capitals in it is right or not.
    We define the usage of capitals in a word to be right when one of the following cases holds:
    -  All letters in this word are capitals, like "USA".
    -  All letters in this word are not capitals, like "leetcode".
    -  Only the first letter in this word is capital, like "Google".
    -  Otherwise, we define that this word doesn't use capitals in a right way.

    Example 1: Input: "USA"    Output: True
    Example 2: Input: "FlaG"   Output: False
    
    Note: The input will be a non-empty word consisting of uppercase 
    and lowercase latin letters.
"""


def detectCapitalUse(word: str) -> bool:
    if not word:
        return True

    first_upper, all_upper, all_lower = False, False, True
    if word[0].isupper():
        first_upper = True
        all_lower = False
    if len(word) > 1:
        if first_upper and word[1].isupper():
            all_upper = True
        elif not first_upper and word[1].isupper():
            return False
    for i in range(2, len(word)):
        if (not all_upper and word[i].isupper()) or (all_upper and word[i].islower()):
            return False

    return first_upper or all_upper or all_lower


def detectCapitalUse_1(word: str) -> bool:
    c = 0
    for i in word:
        if i == i.upper():
            c += 1
    return c == len(word) or (c == 1 and word[0].isupper()) or c == 0


def test_code():
    assert detectCapitalUse('USA')
    assert detectCapitalUse('Vishal')
    assert detectCapitalUse('vishal')
    assert not detectCapitalUse('vishAl')
    assert detectCapitalUse('A')
    assert detectCapitalUse('a')
    assert not detectCapitalUse('FFFFFFFFFFFFFFFFFFFFf')
    assert not detectCapitalUse('mL')
    print("Tests Passed!!")


test_code()
