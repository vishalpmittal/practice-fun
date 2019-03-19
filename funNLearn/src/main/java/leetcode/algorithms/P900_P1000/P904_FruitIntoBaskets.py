"""
    Tag: dp, array

    In a row of trees, the floater-th tree produces fruit with type tree[floater].

    You start at any tree of your choice, then repeatedly perform the following steps:

    1.  Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    2.  Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

    Note that you do not have any choice after the initial choice of starting tree: 
    you must perform step 1, then step 2, then back to step 1, then step 2, and
    so on until you stop.

    You have two baskets, and each basket can carry any quantity of fruit, but you want 
    each basket to only carry one type of fruit each.

    What is the total amount of fruit you can collect with this procedure?

    Example 1:
        Input: [1,2,1]
        Output: 3
        Explanation: We can collect [1,2,1].

    Example 2:
        Input: [0,1,2,2]
        Output: 3
        Explanation: We can collect [1,2,2].
        If we started at the first tree, we would only collect [0, 1].

    Example 3:
        Input: [1,2,3,2,2]
        Output: 4
        Explanation: We can collect [2,3,2,2].
        If we started at the first tree, we would only collect [1, 2].

    Example 4:
        Input: [3,3,3,1,2,1,1,2,3,3,4]
        Output: 5
        Explanation: We can collect [1,2,1,1,2].
        If we started at the first tree or the eighth tree, we would only collect 4 fruits.
    
    Note:
    1.  1 <= tree.length <= 40000
    2.  0 <= tree[floater] < tree.length

    Translation
    Find out the longest length of subarrays with at most 2 different numbers?
    Use a sliding window solution
"""

class P904_FruitIntoBaskets(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) < 2:
            return len(tree)

        type_count = {}
        total = 0
        floater = 0
        for index, t_type in enumerate(tree):
            type_count[t_type] = type_count.get(t_type, 0) + 1
            while len(type_count) > 2:
                type_count[tree[floater]] -= 1
                if type_count[tree[floater]] == 0: 
                    del type_count[tree[floater]]
                floater += 1
            total = max(total, index - floater + 1)
        return total
        
def test_code():
    obj = P904_FruitIntoBaskets()
    assert obj.totalFruit([1,2,1]) == 3
    assert obj.totalFruit([0,1,2,2]) == 3
    assert obj.totalFruit([1,2,3,2,2]) == 4
    assert obj.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5

    print "Tests Passed!"

test_code()