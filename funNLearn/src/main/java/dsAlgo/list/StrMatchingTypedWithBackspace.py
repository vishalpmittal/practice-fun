"""
    tag: list, stack
    
    you are give two strings where # represents a backspace. 
    return whether the srings are equal

    Ex1: output : False
    "abce###" --> "a"
    "b#d#e#f#" --> ""

    Ex2: output : False
    "abce#f##" --> ab
    “#abc” --> abc
"""


def compare_strs(S1: str, S2: str) -> bool:
    if not S1 or not S2:
        return False

    final_typed_S1 = []
    final_typed_S2 = []

    for ch in S1:
        if ch == "#" and len(final_typed_S1) > 0:
            final_typed_S1.pop(len(final_typed_S1) - 1)
        elif ch.isalpha():
            final_typed_S1.append(ch)

    for ch in S2:
        if ch == "#" and len(final_typed_S2) > 0:
            final_typed_S2.pop(len(final_typed_S2) - 1)
        elif ch.isalpha():
            final_typed_S2.append(ch)

    return "".join(final_typed_S1) == "".join(final_typed_S2)


def compare_strs_faster(S1: str, S2: str) -> bool:
    if not S1 or not S2:
        return False

    p1, p2 = len(S1) - 1, len(S2) - 1
    bsc1, bsc2 = 0, 0  # back space count

    while p1 >= 0 or p2 >= 0:
        while p1 >= 0 and (S1[p1] == "#" or bsc1 > 0):
            if S1[p1] == "#":
                bsc1 += 1
            elif bsc1 > 0:
                bsc1 -= 1
            p1 -= 1

        while p2 >= 0 and (S2[p2] == "#" or bsc2 > 0):
            if S2[p2] == "#":
                bsc2 += 1
            elif bsc2 > 0:
                bsc2 -= 1
            p2 -= 1

        if p1 >= 0 and p2 >= 0 and S1[p1] != S2[p2]:
            return False
        else:
            p1 -= 1
            p2 -= 1

    return p1 == p2


assert not compare_strs("abce###", "b#d#e#f#")
assert not compare_strs("abce#f##", "#abc")
assert compare_strs("abce#f##", "#abc#")

assert not compare_strs_faster("abce###", "b#d#e#f#")
assert not compare_strs_faster("abce#f##", "#abc")
assert compare_strs_faster("abce#f##", "#abc#")

print("Tests Passed!")
