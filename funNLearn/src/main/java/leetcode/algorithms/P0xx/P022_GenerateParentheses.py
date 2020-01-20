"""
    Tag: dp, recursive

    Given n pairs of parentheses, write a function to generate all 
    combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:
    [
        "(()())",
        "((()))",
        "(())()",
        "()(())",
        "()()()"
    ]
"""

class Solution(object):

    def generateParenthesis_rec(self, n):
        """
        Recursive solution
        :type n: int
        :rtype: List[str]
        """
        super_set = []
        self.generate_brcks(n, n, "", super_set)
        return super_set

    """
        ----------------
        3 3  []
        ----------------
        2 3 ( []
        ----------------
        1 3 (( []
        ----------------
        0 3 ((( []
        ----------------
        0 2 ((() []
        ----------------
        0 1 ((()) []
        ----------------
        0 0 ((())) []
        ----------------
        1 2 (() ['((()))']
        ----------------
        0 2 (()( ['((()))']
        ----------------
        0 1 (()() ['((()))']
        ----------------
        0 0 (()()) ['((()))']
        ----------------
        1 1 (()) ['((()))', '(()())']
        ----------------
        0 1 (())( ['((()))', '(()())']
        ----------------
        0 0 (())() ['((()))', '(()())']
        ----------------
        2 2 () ['((()))', '(()())', '(())()']
        ----------------
        1 2 ()( ['((()))', '(()())', '(())()']
        ----------------
        0 2 ()(( ['((()))', '(()())', '(())()']
        ----------------
        0 1 ()(() ['((()))', '(()())', '(())()']
        ----------------
        0 0 ()(()) ['((()))', '(()())', '(())()']
        ----------------
        1 1 ()() ['((()))', '(()())', '(())()', '()(())']
        ----------------
        0 1 ()()( ['((()))', '(()())', '(())()', '()(())']
        ----------------
        0 0 ()()() ['((()))', '(()())', '(())()', '()(())']

        ['((()))', '(()())', '(())()', '()(())', '()()()']
    """
    def generate_brcks(self, leftRemaining, rightRemaining, curr_str, super_set):
        
        # print ("----------------\n{} {} {} {}".format(
        #     leftRemaining, rightRemaining, curr_str, super_set
        #     ))

        # If we are left with 0 left and 0 right brackets to put. 
        # add curr_str and return
        if (leftRemaining == 0 and rightRemaining == 0):
            super_set.append(curr_str)
            return super_set

        # add a left parenthesis first in every call, as right can not be added without it
        # recurse with added left parenethesis. eg:
        # initial curr_str : (
        # resurse over curr_str: ((
        if leftRemaining > 0:
            self.generate_brcks(leftRemaining-1, rightRemaining, curr_str+'(', super_set)

        # for same curr_str add a right only if there are enough left's added. 
        # remember for the current call curr_str has not changed here 
        # recurse with added right parenethesis. eg:
        # initial curr_str: (
        # recurse over curr_str: ()
        if leftRemaining < rightRemaining:
            self.generate_brcks(leftRemaining, rightRemaining-1, curr_str+')', super_set)

    def generateParenthesis_dp(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # create a list of empty lists. 
        dp = [[] for i in range(n + 1)]

        # add empty string in the first list
        dp[0].append('')

        # update 1st list based on all elements of 0th list.
        # update 2nd list based on all elements of 0th and 1st list..
        # and so on...
        for i in range(1, n + 1):
            for j in range(i):
                print ("------ i={} j={} ".format(i, j))
                print (dp)
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

def test_code():
    obj = Solution()
    # print obj.generateParenthesis_rec(3)
    print (obj.generateParenthesis_dp(4))

test_code()
