"""
    Tag: string, array

    Given an array of characters, compress it in-place.
    - The length after compression must always be smaller than or equal to the original array.
    - Every element of the array should be a character (not int) of length 1.
    - After you are done modifying the input array in-place, return the new length of the array.

    Follow up:
    Could you solve it using only O(1) extra space?

    Example 1:
    Input: ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: 
            ["a","2","b","2","c","3"]
    Explanation: "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
    
    Example 2:
    Input: ["a"]
    Output: Return 1, and the first 1 characters of the input array should be: ["a"]
    Explanation: Nothing is replaced.
    
    Example 3:
    Input: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation: Since the character "a" does not repeat, it is not compressed. 
            "bbbbbbbbbbbb" is replaced by "b12". 
            Notice each digit has it's own entry in the array.

    Note:
    - All characters have an ASCII value in [35, 126]. 
    - 1 <= len(chars) <= 1000.
"""
from typing import List


def compress(chars: List[str]) -> int:
    if not chars or len(chars) < 2:
        return 0 if not chars else len(chars)

    chars_iter, new_len, curr_char_count = 1, 1, 1
    while chars_iter < len(chars):
        if chars[chars_iter] == chars[chars_iter-1]:
            curr_char_count += 1
        else:
            if curr_char_count > 1:
                for cnt_digit in str(curr_char_count):
                    chars[new_len] = cnt_digit
                    new_len += 1
            chars[new_len] = chars[chars_iter]
            new_len += 1
            curr_char_count = 1
        chars_iter += 1
    
    if curr_char_count > 1:
        for cnt_digit in str(curr_char_count):
            chars[new_len] = cnt_digit
            new_len += 1
    return new_len


def test_code():
    test_chars = [
        ["a","a","b","b","c","c","c"], 
        ["a"], 
        ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    ]
    result_rets = [6, 1, 4]
    result_chars = [
        ["a","2","b","2","c","3","c"], 
        ["a"], 
        ["a","b","1","2","b","b","b","b","b","b","b","b","b"]
    ]

    for i in range(len(test_chars)):
        assert compress(test_chars[i]) == result_rets[i]
        assert test_chars[i] == result_chars[i]

    print("Tests Passed!!")

test_code()
