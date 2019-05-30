"""
    Tag: string, integer

    Given two non-negative integers num1 and num2 represented as strings, 
    return the product of num1 and num2, also represented as a string.

    Example 1: Input: num1 = "2", num2 = "3", Output: "6"
    
    Example 2: Input: num1 = "123", num2 = "456", Output: "56088"
    
    Note:
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

    Approach:
    simulate old school multiplication here. 
    `num1[i] * num2[j]` will be placed at indices `[i + j, i + j + 1]`
    example: 4(index 0), and 2 index (1) result is placed at index 1 (0) and index 2 (8)
    we can traverse each digit and convert via ascii and put them in result.

            1   2   3 
                4   5
    ---------------------
                1   5
            1   0
        0   5
                    X
            1   2
        0   8
    0   4
    ---------------------
        5   5   3   5
    ---------------------
        
"""


class Solution(object):
    @staticmethod
    def char2int(ch):
        return ord(ch) - ord('0')

    @staticmethod
    def int2char(num):
        return chr(num + ord('0'))

    @staticmethod
    def multiply(num1, num2):
        l1, l2 = len(num1), len(num2)
        answer = [0] * (l1 + l2)

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                mul = Solution.char2int(num1[i]) * Solution.char2int(num2[j])

                pos1, pos2 = i + j, i + j + 1
                s = mul + answer[pos2]
                answer[pos1] += s / 10
                answer[pos2] = (s) % 10
        str_answer = ''
        for a in answer:
            if not (len(str_answer) == 0 and a == 0):
                str_answer += Solution.int2char(a)
        return str_answer

def test_code():
    assert Solution.multiply('123', '45') == '5535'
    print 'tests passed!!'

test_code()