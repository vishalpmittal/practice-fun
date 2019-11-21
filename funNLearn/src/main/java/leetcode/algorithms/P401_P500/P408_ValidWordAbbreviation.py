"""
    Tag: string, array

    Given a non-empty string s and an abbreviation abbr, return whether the string matches with 
    the given abbreviation.

    A string such as "word" contains only the following valid abbreviations:
    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", 
    "2r1", "3d", "w3", "4"]
    
    Notice that only the above abbreviations are valid abbreviations of the string "word". 
    Any other string is not a valid abbreviation of "word".

    Note: Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

    Example 1: Given s = "internationalization", abbr = "i12iz4n": 
                Return true.
    
    Example 2: Given s = "apple", abbr = "a2e":
                Return false.
"""

def validWordAbbreviation(word: str, abbr: str) -> bool:
    if not word or not abbr:
        return False
    
    w, a = 0, 0
    while w < len(word) and a < len(abbr):
        if word[w] == abbr[a]: 
            w+=1
            a+=1
        elif abbr[a].isdigit() and int(abbr[a])!=0:
            a_num = abbr[a]
            a += 1
            while a<len(abbr) and abbr[a].isdigit():
                a_num = a_num + '' + abbr[a]
                a+=1
            if w + int(a_num) > len(word):
                return False
            w += int(a_num)
        else: return False
        # print('w: {}, a: {}'.format(w, a))

    if w < len(word) or a < len(abbr):
        return False
    return True

def test_code():
    assert validWordAbbreviation('internationalization', 'i12iz4n') == True
    assert validWordAbbreviation('internationalization', 'i5a11o1') == True
    assert validWordAbbreviation('a', '01') == False
    assert validWordAbbreviation('hi', 'hi1') == False
    assert validWordAbbreviation('apple', 'a2e') == False
    print ("Tests Passed!!")

test_code()
