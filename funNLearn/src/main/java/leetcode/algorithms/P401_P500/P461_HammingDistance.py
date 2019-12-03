"""
    Tag: bit
    
    The Hamming distance between two integers is the number of positions at which 
    the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.

    Note: 0 ≤ x, y < 231.

    Example: Input: x = 1, y = 4,  Output: 2
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
"""

def hammingDistance(x: int, y: int) -> int:
    return bin(x^y).count('1')

def test_code():
    assert hammingDistance(1, 4) == 2
    print ("Tests Passed!!")

test_code()
