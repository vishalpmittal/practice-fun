"""
    Tag: array, integer, bit

    Given two binary strings, return their sum (also a binary string).
    The input strings are both non-empty and contains only characters 1 or 0.

    Examples:
    Input: a = "11", b = "1", Output: "100"
    Input: a = "1010", b = "1011", Output: "10101"
"""


def char2int(ch):
    return ord(ch) - ord('0')


def int2char(num):
    return chr(num + ord('0'))


def addBinary(a, b):
    if not a or not b:
        return 0
    i, bsum, carry = 1, '', 0
    while i <= len(a) or i <= len(b):
        sum = carry 
        if i <= len(a): sum += char2int(a[-i])
        if i <= len(b): sum += char2int(b[-i])
        bsum = int2char(sum % 2) + bsum
        carry = sum / 2
        i += 1
    return bsum if i == 0 else int2char(carry) + bsum


def test_code():
    assert addBinary('1010', '1011') == '10101'
    assert addBinary('11', '1') == '100'
    print ('Tests Passed!!')


test_code()
