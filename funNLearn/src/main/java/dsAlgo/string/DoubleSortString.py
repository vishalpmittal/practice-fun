"""
    tag: sort, string

    given a string, return a new string which has the character sorted by 
    count first and then by order of occurance in the given string. 
    
    Input: 'bbbcceeddaf'
    Output: 'afcceeddbbb'
"""
from collections import OrderedDict
from collections import Counter


class Solution:
    def arrange_str(self, S: str) -> str:
        if not S:
            return S

        char_to_count_dict = OrderedDict()
        for c in S:
            char_to_count_dict[c] = char_to_count_dict.get(c, 0) + 1

        count_to_charList_dict = {}
        for char, cnt in char_to_count_dict.items():
            count_to_charList_dict[cnt] = count_to_charList_dict.get(cnt, [])
            count_to_charList_dict[cnt].append(char)
        char_to_count_dict = None

        ans_str = ""
        for cnt in sorted(count_to_charList_dict.keys()):
            for c in count_to_charList_dict[cnt]:
                ans_str += c * cnt
        return ans_str

    def arrange_str2(self, S: str) -> str:
        char_cnt = Counter(S)
        char_position = {S[i]: i for i in range(len(S) - 1, -1, -1)}
        S = sorted(S, key=lambda x: char_position[x])
        S = sorted(S, key=lambda x: char_cnt[x])
        return "".join(S)


assert Solution().arrange_str("bbbcceeddaf") == "afcceeddbbb"
assert Solution().arrange_str("david") == "avidd"

assert Solution().arrange_str2("bbbcceeddaf") == "afcceeddbbb"
assert Solution().arrange_str2("david") == "avidd"

print("Tests Passed!!!")
