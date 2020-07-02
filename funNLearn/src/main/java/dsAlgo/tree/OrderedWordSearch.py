"""
    Background:
    You have a dictionary that includes words within a special order 
    and the order of those words is very important for you. 

    Objective
    You want to search your words like a Google Seach and want to get 
    the matching words with the same order as in your dictionary. When you 
    run your dictionary app, it will always welcome any input and the matching 
    results will be output after pressing enter.

    Input Data:
    You are provided a string variable into your code like this;
    yourdictionary = ["Alim", "Velime", "Deline", "Almakan", "Delmekin", "Vermekine", "Ala", "Vilpan"]

    Test1: Al
    Alim
    Almakan
    Ala

    Test2: V
    Velime
    Vermekine
    Vilpan
"""


class TNode:
    def __init__(self, val):
        self.val = val
        self.next = list()

    def __str__(self):

        st = "["
        for ch_node in self.next:
            st += str(ch_node)

        return str(self.val) + "->" + st + "]"

    def get_child(self, ch_val):
        for child in self.next:
            if child.val == ch_val:
                return child

        return None

    def get_possible_sub_words(self, ss):
        word_list = []

        def helper(node, curr_word):
            if not node.next:
                word_list.append(curr_word)
                return

            for ch_node in node.next:
                helper(ch_node, curr_word + ch_node.val)

        helper(self, ss)
        return word_list


search_dict = TNode(None)


def build_ord_dict(word_set):
    for word in word_set:
        curr_node = search_dict

        for ch in word:
            child_node = curr_node.get_child(ch.lower())

            if not child_node:
                child_node = TNode(ch.lower())
                curr_node.next.append(child_node)

            curr_node = child_node


def search_str(ss):
    curr_node = search_dict

    if not ss or not curr_node.get_child(ss[0].lower()):
        return []

    i = 0
    while curr_node and i < len(ss):
        curr_node = curr_node.get_child(ss[i].lower())
        i += 1

    if not curr_node:
        return []

    return curr_node.get_possible_sub_words(ss)


build_ord_dict(
    ["Alim", "Velime", "Deline", "Almakan", "Delmekin", "Vermekine", "Ala", "Vilpan"]
)

assert search_str("a") == ["alim", "almakan", "ala"]
assert search_str("al") == ["alim", "almakan", "ala"]
assert search_str("ali") == ["alim"]
assert search_str("alm") == ["almakan"]
assert search_str("ve") == ["velime", "vermekine"]
assert search_str("de") == ["deline", "delmekin"]
assert search_str("v") == ["velime", "vermekine", "vilpan"]
assert search_str("vishal") == []
assert search_str("") == []
assert search_str(None) == []


print("Tests Passed!!!")
