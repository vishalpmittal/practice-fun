"""
    Tag: recursive, array

    Given a string containing digits from 2-9 inclusive, return all 
    possible letter combinations that the number could represent.

    A mapping of digit to letters (just like on the telephone buttons) is 
    given below. Note that 1 does not map to any letters.

    Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    
    Note:
    Although the above answer is in lexicographical order, your answer
    could be in any order you want.
"""

class P017_LetterCombinationsOfAPhoneNumber(object):

    def letterCombinations(self, digits):
        """
        recursive solution:
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # base conditions
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])

        # recurse over last but one of digits    
        prev = self.letterCombinations(digits[:-1])

        # combine prev result string set and last numbers char sets
        return [s + c for s in prev for c in mapping[digits[-1]]]

def test_code():
    obj = P017_LetterCombinationsOfAPhoneNumber()
    assert obj.letterCombinations('23') == [
            "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
        ]
    print ("Tests Passed!")

test_code()