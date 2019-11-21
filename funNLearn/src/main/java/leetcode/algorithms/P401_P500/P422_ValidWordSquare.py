"""
    Tag: string, array, matrix

    Given a sequence of words, check whether it forms a valid word square.

    A sequence of words forms a valid word square if the kth row and column 
    read the exact same string, where 0 ≤ k < max(numRows, numColumns).

    Note:
    The number of words given is at least 1 and does not exceed 500.
    Word length will be at least 1 and does not exceed 500.
    Each word contains only lowercase English alphabet a-z.
    
    Example 1:
    Input: [ "abcd", "bnrt", "crmy", "dtye" ]
    Output: true
    Explanation: 
    The first row and first column both read "abcd".
    The second row and second column both read "bnrt".
    The third row and third column both read "crmy".
    The fourth row and fourth column both read "dtye".

    Example 2:
    Input: [ "abcd", "bnrt", "crm", "dt" ]
    Output: true
    Explanation:
    The first row and first column both read "abcd".
    The second row and second column both read "bnrt".
    The third row and third column both read "crm".
    The fourth row and fourth column both read "dt".

    Example 3:
    Input: [ "ball", "area", "read", "lady"]
    Output: false
    Explanation: The third row reads "read" while the third column reads "lead".
"""

def validWordSquare(words: List[str]) -> bool:
    """
    recreate the word list by taking 1st char of all words, then 2nd and so on.
    compare the two lists at the end.
    """
    ref = []
    for i in range(len(words)):
        tmp = ""
        for j in words:
            if i < len(j):
                tmp += j[i]
        ref.append(tmp)
    return ref == words

from itertools import zip_longest 
def validWordSquare_1(words: List[str]) -> bool:
    """
    zip(*words) is a commonly used Python trick to transpose a matrix. 
    zip_longest is used in place of zip for stirngs of different lengths, 
    e.g. words = ["abcd","bnrt","crm","dt"].

    >>> list(zip(*words))
    [('a', 'b', 'c', 'd'), ('b', 'n', 'r', 't')]
    >>> list(zip_longest(*words))
    [('a', 'b', 'c', 'd'), ('b', 'n', 'r', 't'), ('c', 'r', 'm', None), ('d', 't', None, None)]
    >>> list(zip(*words))
    [('a', 'b', 'c', 'd'), ('b', 'n', 'r', 't')]
    >>> list(zip_longest(*words))
    [('a', 'b', 'c', 'd'), ('b', 'n', 'r', 't'), ('c', 'r', 'm', None), ('d', 't', None, None)]
    """
    return words == ["".join(filter(None, x)) for x in zip_longest(*words)]


def test_code():
    assert validWordSquare([ "abcd", "bnrt", "crmy", "dtye" ]) == True
    print ("Tests Passed!!")

test_code()
