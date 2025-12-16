"""
    tag: string, sliding window, longest substring

    ----------------------------------------------
    Longest Substring Without Repeating Characters
    ----------------------------------------------
    Given a string s, find all longest substrings without repeating characters.

    Input: s = ""
    Output: []

    Input: s = "yyyyy"
    Output: ["y"]
    Explanation: The answer is ["y"], with the length of 1.

    Input: s = "wzzpuz"
    Output: "zpu", "puz"
    Explanation: The answer is both "zpu" and "puz", each with the length of 3.

    Input: s = "abcdaxyzbcx"
    Output: ["bcdaxyz", "cdaxyzb"]
    Explanation: The answer is ["bcdaxyz", "cdaxyzb"], with the length of 7.
"""
from typing import List


def longest_substrings(s: str) -> List[str]:
    """Return all longest substrings without repeating characters.

    Uses a sliding-window with last-seen indices to run in O(n) time and O(k) space. Returns substrings in the order they are discovered.
    """
    if not s:
        return []

    last = {}  # char -> last index seen
    left = 0
    maxlen = 0
    results: List[str] = []

    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1

        cur_len = right - left + 1
        if cur_len > maxlen:
            maxlen = cur_len
            results = [s[left:right + 1]]
        elif cur_len == maxlen:
            results.append(s[left:right + 1])

        last[ch] = right

    return results


if __name__ == "__main__":
    tests = [
        ("", []),
        ("yyyyy", ["y"]),
        ("wzzpuz", ["zpu", "puz"]),
        ("abcdaxyzbcx", ["bcdaxyz", "cdaxyzb", "daxyzbc"]),
    ]

    for inp, expected in tests:
        out = longest_substrings(inp)
        print(f"s={inp!r}\n  -> {out}\n  expected: {expected}\n")

