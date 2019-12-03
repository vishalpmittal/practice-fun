"""
    Tag: bit

    Given a positive integer, output its complement number. 
    The complement strategy is to flip the bits of its binary representation.

    Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
    
    Example 1: Input: 5, Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), 
    and its complement is 010. So you need to output 2.

    Example 2: Input: 1, Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), 
    and its complement is 0. So you need to output 0.
"""

def findComplement(self, num):
    """
        Find the binary length of number 
        num i = i<<1 keeps moving i to 1, 2, 4, 8, 16,.... nearest to num
        eg. then i=8 is 1000 i-1 =7 is 111
        xor (i-1) with num gives the complement of the number
    """
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num

def test_code():
    assert findComplement() == True
    print ("Tests Passed!!")

test_code()
