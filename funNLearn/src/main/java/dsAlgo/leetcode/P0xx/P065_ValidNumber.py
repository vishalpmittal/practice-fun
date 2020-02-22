"""
    Tag: string, integer, algo, DFA (Deterministic Finite Automata / tion)

    Validate if a given string can be interpreted as a decimal number.
    Some examples:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true
    " -90e3   " => true
    " 1e" => false
    "e3" => false
    " 6e-1" => true
    " 99e2.5 " => false
    "53.5e93" => true
    " --6 " => false
    "-+3" => false
    "95a54e53" => false

    Note: It is intended for the problem statement to be ambiguous. 
    You should gather all requirements up front before implementing one. 
    However, here is a list of characters that can be in a valid decimal number:
    
    Numbers 0-9
    Exponent - "e"
    Positive/negative sign - "+"/"-"
    Decimal point - "."
    
    Of course, the context of these characters also matters in the input.
"""
from typing import List


class Solution:
    def isNumber(self, s: str) -> bool:
        state = [
            {},
            {"blank": 1, "sign": 2, "digit": 3, ".": 4},
            {"digit": 3, ".": 4},
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            {"digit": 5},
            {"digit": 5, "e": 6, "blank": 9},
            {"sign": 7, "digit": 8},
            {"digit": 8},
            {"digit": 8, "blank": 9},
            {"blank": 9},
        ]
        currentState = 1
        for c in s:
            if c >= "0" and c <= "9":
                c = "digit"
            if c == " ":
                c = "blank"
            if c in ["+", "-"]:
                c = "sign"
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3, 5, 8, 9]:
            return False
        return True


assert not Solution().isNumber("4e+")
assert Solution().isNumber("0")
assert Solution().isNumber(" 0.1 ")
assert not Solution().isNumber("abc")
assert not Solution().isNumber("1 a")
assert Solution().isNumber("2e10")
assert Solution().isNumber(" -90e3   ")
assert not Solution().isNumber(" 1e")
assert not Solution().isNumber("e3")
assert Solution().isNumber(" 6e-1")
assert not Solution().isNumber(" 99e2.5 ")
assert Solution().isNumber("53.5e93")
assert not Solution().isNumber(" --6 ")
assert not Solution().isNumber("-+3")
assert not Solution().isNumber("95a54e53")
assert Solution().isNumber(".3")
assert Solution().isNumber("3.")
print("Tests Passed!!")
