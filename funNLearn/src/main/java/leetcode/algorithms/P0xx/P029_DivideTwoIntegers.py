"""
    Tag: math, bit

    Given two integers dividend and divisor, divide two integers 
    without using multiplication, division and mod operator.

    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.

    Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3

    Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2

    Note:
    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.

    Assume we are dealing with an environment which could only store
    integers withing the 32-bit signed integer range [-2^31 to 2^31-1]
    For the purpose of this problem, assume that your function returns
    [2^31 -1] when the division result overflows.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
            basic method:
            substract the divisor from dividend as long as dividend > divisor

            faster:
            During each iteration of basic method, double the substraction. Like:

            ret = 0;
            17-2, ret+=1; left=15
            15-4, ret+=2; left=11
            11-8, ret+=4; left=3
            3-2, ret+=1; left=1
            ret=8;

            but without multiplication how to double the iterating number ?
            use bit operation. 

            << : left shift is equivalent to *2 
            >> : right shift is equivalent to /2

            eg:
            sub=17
            bin(sub) = '0b10001' = 17
            bin(sub<<1) = '0b100010' = 34
        """
        isMinus= ((dividend<0 and divisor >0) or (dividend>0 and divisor <0))
        ret=0
        dividend, divisor=abs(dividend), abs(divisor)
        power = 1
        sub = divisor

        while(dividend >= divisor):
            if(dividend>=sub):
                dividend-=sub
                ret+=power
                sub=(sub<<1)
                power=(power<<1)
            else:
                sub=(sub>>1)
                power=(power>>1)
        
        if(isMinus):
            ret=-ret
        return min(max(-2147483648,ret),2147483647)


def test_code():
    obj = Solution()
    assert obj.divide(17, 3) == 5
    assert obj.divide(7, -3) == -2
    assert obj.divide(-24, -5) == 4
    print ("Tests Passed!")

test_code()
