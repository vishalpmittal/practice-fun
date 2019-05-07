"""
    Tag: integer

    The count-and-say sequence is the sequence of integers with the 
    first five terms as following:
    1. 1
    2. 11
    3. 21
    4. 1211
    5. 111221
    6. 312211
    7. 13112221
    8. 1113213211
    9. 31131211131221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 <= n <= 30, generate the nth term of the count-and-say sequence.
    Note: Each term of the sequence of integers will be represented as a string.


    Example 1:
    Input: 1, Output: "1"
    
    Example 2:
    Input: 4, Output: "1211"
"""

class Solution(object):
    @staticmethod
    def solve_problem(n):
        curr_cns = '1'
        for x in range(0, n-1):
            curr_cns = Solution.count_n_say(curr_cns)
        return curr_cns

    @staticmethod
    def count_n_say(ip_nums):
        if not ip_nums: return ''

        n = ip_nums[0]
        c = 1
        cns = ''
        for i in range (1, len(ip_nums)):
            if ip_nums[i] == n:
                c += 1
            else:
                cns += str(c) + str(n)
                c = 1
                n = ip_nums[i]
        
        return cns + str(c) + str(n)
        
def test_code():
    assert Solution.solve_problem(1) == '1'
    assert Solution.solve_problem(2) == '11'
    assert Solution.solve_problem(3) == '21'
    assert Solution.solve_problem(4) == '1211'
    assert Solution.solve_problem(5) == '111221'
    assert Solution.solve_problem(6) == '312211'
    assert Solution.solve_problem(7) == '13112221'
    assert Solution.solve_problem(8) == '1113213211'
    assert Solution.solve_problem(9) == '31131211131221'
    print 'Tests Passed!'

test_code()
