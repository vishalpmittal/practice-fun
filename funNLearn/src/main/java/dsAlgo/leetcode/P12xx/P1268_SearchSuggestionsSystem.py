"""
    tag: trie, recursion

    Given an array of strings products and a string searchWord. We want to design 
    a system that suggests at most three product names from products after each 
    character of searchWord is typed. Suggested products should have common prefix 
    with the searchWord. If there are more than three products with a common prefix 
    return the three lexicographically minimums products.

    Return list of lists of the suggested products after each character of searchWord is typed. 

    Example 1: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
    ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

    Example 2: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

    Example 3: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

    Example 4: products = ["havana"], searchWord = "tatiana"
    Output: [[],[],[],[],[],[],[]]

    Constraints:
    - 1 <= products.length <= 1000
    - There are no repeated elements in products.
    - 1 <= Σ products[i].length <= 2 * 10^4
    - All characters of products[i] are lower-case English letters.
    - 1 <= searchWord.length <= 1000
    - All characters of searchWord are lower-case English letters.
"""
from collections import OrderedDict
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:

        SD = dict()  # search dictionary

        def create_search_dict():
            products.sort()

            for prod in products:
                curr_lvl_dict = SD
                for c in prod:
                    curr_lvl_dict[c] = curr_lvl_dict.get(c, dict())
                    curr_lvl_dict = curr_lvl_dict[c]
                curr_lvl_dict[1] = 1

        def get_search_str_level_dict(curr_str):
            if curr_str[0] not in SD:
                return {}

            curr_dict = SD
            for c in curr_str:
                if c not in curr_dict:
                    return curr_dict
                curr_dict = curr_dict[c]
            return curr_dict

        def get_word_suggestions(word, word_sugg_dict, sugg_list, n):
            if len(sugg_list) == n:
                return

            if 1 in word_sugg_dict:
                sugg_list.append(word)
                if len(word_sugg_dict.keys()) == 1:
                    return

            for key, new_dict in word_sugg_dict.items():
                if key == 1:
                    continue
                get_word_suggestions(word + key, new_dict, sugg_list, n)

        create_search_dict()
        curr_search_str = ""
        result_lol = []
        for c in searchWord:
            curr_search_str += c
            curr_search_str_dict = get_search_str_level_dict(curr_search_str)
            curr_word_sugg_list = []
            get_word_suggestions(
                curr_search_str, curr_search_str_dict, curr_word_sugg_list, 3
            )
            result_lol.append(curr_word_sugg_list)
        return result_lol


print(
    Solution().suggestedProducts(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse",
    )
)
print(Solution().suggestedProducts(["havana"], "havana"))

print(
    Solution().suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], "bags")
)
print(Solution().suggestedProducts(["havana"], "tatiana"))
