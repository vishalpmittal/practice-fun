"""
    Tag: math

    Given an integer, return its base 7 string representation.
    Example 1: Input: 100 Output: "202"
    Example 2: Input: -7 Output: "-10"

    Note: The input will be in range of [-1e7, 1e7].
"""


def val(num: int) -> chr:
    # chr() and ord() are inverse of each other
    # ord('a')=97 while chr('97')=a
    if 0 <= num <= 9:
        return chr(num + ord('0'))
    return chr(num - 10 + ord('A'))


def convertToBase7(x: int) -> str:
    is_neg = False
    if x < 0:
        is_neg = True
    x = abs(x)
    ans = ''
    while x > 0:
        ans += val(x % 7)
        x = x // 7
    if not is_neg:
        return ans[::-1]
    return '-' + ans[::-1]


def test_code():
    assert convertToBase7(100) == 202
    assert convertToBase7(-7) == -10
    print("Tests Passed!!")


test_code()
