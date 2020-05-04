"""
    tag: sliding window, string

    Given a string S and a string T, find the minimum window in S which 
    will contain all the characters in T in complexity O(n).

    Example: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"

    Note:
    - If there is no such window in S that covers all characters in T, 
      return the empty string "".
    - If there is such window, you are guaranteed that there will always 
      be only one unique minimum window in S.


    Algorithm
    1. We start with two pointers, leftleft and rightright initially pointing 
       to the first element of the string SS.
    2. We use the rightright pointer to expand the window until we get a desirable 
       window i.e. a window that contains all of the characters of TT.
    3. Once we have a window with all the characters, we can move the left pointer 
       ahead one by one. If the window is still a desirable one we keep on updating 
       the minimum window size.
    4. If the window is not desirable any more, we repeat step 2 onwards.
"""
from typing import List
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_char_count_dic = Counter(t)
        t_no_uniq_chars = len(t_char_count_dic)
        lp, rp = 0, 0  # left pointer, right pointer

        UCOT_ICW = 0  # unique character of t in current window
        window_counts = {}  # count of unique characters in current window

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while rp < len(s):
            character = s[rp]
            window_counts[character] = window_counts.get(character, 0) + 1

            if (
                character in t_char_count_dic
                and window_counts[character] == t_char_count_dic[character]
            ):
                UCOT_ICW += 1

            while lp <= rp and UCOT_ICW == t_no_uniq_chars:
                character = s[lp]

                if rp - lp + 1 < ans[0]:
                    ans = (rp - lp + 1, lp, rp)

                window_counts[character] -= 1
                if (
                    character in t_char_count_dic
                    and window_counts[character] < t_char_count_dic[character]
                ):
                    UCOT_ICW -= 1

                lp += 1

            rp += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
