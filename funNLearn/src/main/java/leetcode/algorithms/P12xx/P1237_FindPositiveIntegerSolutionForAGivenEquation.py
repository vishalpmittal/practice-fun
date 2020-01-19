"""
    Tag: design ds

    Given a function  f(x, y) and a value z, return all positive 
    integer pairs x and y where f(x,y) == z.

    The function is constantly increasing, i.e.:
    -  f(x, y) < f(x + 1, y)
    -  f(x, y) < f(x, y + 1)

    The function interface is defined like this: 
    interface CustomFunction {
    public:
    // Returns positive integer f(x, y) for any given positive integer x and y.
        int f(int x, int y);
    };

    For custom testing purposes you're given an integer function_id and a 
    target z as input, where function_id represent one function from an secret 
    internal list, on the examples you'll know only two functions from the list.  

    You may return the solutions in any order.

    Ex1: i/p: function_id = 1, z = 5 Out: [[1,4],[2,3],[3,2],[4,1]]
    Explanation: function_id = 1 means that f(x, y) = x + y

    Ex2: i/p: function_id = 2, z = 5 Out: [[1,5],[5,1]]
    Explanation: function_id = 2 means that f(x, y) = x * y

    Constraints:
    -  1 <= function_id <= 9
    -  1 <= z <= 100
    -  It's guaranteed that the solutions of f(x, y) == z will be 
       on the range 1 <= x, y <= 1000
    -  It's also guaranteed that f(x, y) will fit in 32 bit signed 
       integer if 1 <= x, y <= 1000
"""
from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        y = 1000
        for x in xrange(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                res.append([x, y])
        return res


assert Solution().findSolution()
print('Tests Passed!!')
