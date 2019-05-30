"""
    Tag: TO-DO,string, algo, finite-state machine, State machine, finite-state automaton (FSA), 
        finite automaton


    Given an input string (s) and a pattern (p), implement wildcard 
    pattern matching with support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    
    The matching should cover the entire input string (not partial).
    
    Note:
    -  s could be empty and contains only lowercase letters a-z.
    -  p could be empty and contains only lowercase letters a-z, and characters like ? or *.
    
    Examples:
    Input: s = "aa", p = "a"    Output: false
    Explanation: "a" does not match the entire string "aa".

    Input: s = "aa", p = "*"    Output: true
    Explanation: '*' matches any sequence.

    Input: s = "cb", p = "?a"   Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

    Input: s = "adceb", p = "*a*b"  Output: true
    Explanation: The first '*' matches the empty sequence, while the 
    second '*' matches the substring "dce".
    
    Input: s = "acdcb", p = "a*c?b"    Output: false
    """


def isMatch(s, patt):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        transfer = {}
        state = 0
        
        for p in patt:
            if p == '*':
                transfer[state, p] = state
            else:
                transfer[state, p] = state + 1
                state += 1
        
        accept = state
        state = set([0])
        
        print 'transfer: {}'.format(transfer)
        print 'accept: {}'.format(accept)
        print 'state: {}'.format(state)

        for char in s:
            state = set([transfer.get((at, token)) for at in state for token in [char, '*', '?']])

        print 'accept: {}'.format(accept)
        print 'state: {}'.format(state)

        return accept in state


def test_code():
    print isMatch('abcdefg', 'ab?d*g')


test_code()

