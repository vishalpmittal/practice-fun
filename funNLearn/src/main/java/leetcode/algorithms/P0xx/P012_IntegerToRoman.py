"""
    Tag: math

    Roman numerals are represented by seven different symbols: 
    I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    
    For example, two is written as II in Roman numeral, just two one's 
    added together. Twelve is written as, XII, which is simply X + II. 
    The number twenty seven is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left 
    to right. However, the numeral for four is not IIII. Instead, 
    the number four is written as IV. Because the one is before the 
    five we subtract it making four. The same principle applies to the 
    number nine, which is written as IX. There are six instances 
    where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    
    Given an integer, convert it to a roman numeral. Input is 
    guaranteed to be within the range from 1 to 3999.

    Ex 1:    Input: 3,   Output: "III"
    Ex 2:    Input: 4    Output: "IV"
    Ex 3:    Input: 9    Output: "IX"
    Ex 4:    Input: 58    Output: "LVIII"
             Explanation: L = 50, V = 5, III = 3.
    Ex 5:    Input: 1994    Output: "MCMXCIV"
             Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class PI012_IntegerToRoman(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dig = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_set = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_str = ""
        i = 0
        while i < len(roman_dig):
            while (num >= roman_dig[i]):
                num -= roman_dig[i]
                roman_str += roman_set[i]
            i+=1
        return roman_str

def test_code():
    obj = PI012_IntegerToRoman()
    assert obj.intToRoman(500)=='D'
    assert obj.intToRoman(3)=='III'
    assert obj.intToRoman(4)=='IV'
    assert obj.intToRoman(9)=='IX'
    assert obj.intToRoman(58)=='LVIII'
    assert obj.intToRoman(1994)=='MCMXCIV'
    print ("Tests Passed!")

test_code()