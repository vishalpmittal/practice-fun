"""
    Tag: TO-DO, string, dp, array, integer, bit, linked list
    Tag: tree, sort, math, matrix, regex, recursive
    Tag: design ds (design data structure), dfs, binary search, algo, game

    Given a list of scores of different students, return the average 
    score of each student's top five scores in the order of each student's id.

    Each entry items[i] has items[i][0] the student's id, and items[i][1] 
    the student's score.  The average score is calculated using integer division.

    Example 1:
    Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    Output: [[1,87],[2,88]]
    Explanation: 
    -  The average of the student with id = 1 is 87.
    -  The average of the student with id = 2 is 88.6. 
    But with integer division their average converts to 88.

    Note:
    -  1 <= items.length <= 1000
    -  items[i].length == 2
    -  The IDs of the students is between 1 to 1000
    -  The score of the students is between 1 to 100
    -  For each student, there are at least 5 scores
"""
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)
        res, curr, idx = [], [], items[0][0]
        idx = items[0][0]
        for i, val in items:
            if i == idx:
                if len(curr) < 5:
                    curr.append(val)
            else:
                res.append([idx, sum(curr) // len(curr)])
                curr = [val]
                idx = i

        res.append([idx, sum(curr) // len(curr)])
        res = res[::-1]
        return res

    def highFive_1(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for idx, val in items:
            heapq.heappush(d[idx], val)
            if len(d[idx]) > 5:
                heapq.heappop(d[idx])
        return [[i, sum(d[i]) // len(d[i])] for i in sorted(d)]


assert Solution().highFive(
    [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77],
        [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
) == [[1, 87], [2, 88]]
print('Tests Passed!!')
