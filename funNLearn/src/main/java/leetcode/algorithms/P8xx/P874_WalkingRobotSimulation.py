"""
    Tag: game

    A robot on an infinite grid starts at point (0, 0) and faces north.  
    The robot can receive one of three possible types of commands:
    -  -2: turn left 90 degrees
    -  -1: turn right 90 degrees
    -  1 <= x <= 9: move forward x units

    Some of the grid squares are obstacles.
    The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

    If the robot would try to move onto them, the robot stays on the 
    previous grid square instead (but still continues following the rest 
    of the route.)

    Return the square of the maximum Euclidean distance that the robot 
    will be from the origin.

    Example 1: Input: commands = [4,-1,3], obstacles = [] Output: 25
    Explanation: robot will go to (3, 4)

    Example 2: Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]] Output: 65
    Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

    Note:
    -  0 <= commands.length <= 10000
    -  0 <= obstacles.length <= 10000
    -  -30000 <= obstacle[i][0] <= 30000
    -  -30000 <= obstacle[i][1] <= 30000
    -  The answer is guaranteed to be less than 2 ^ 31.
"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        rt = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
        lt = {'u': 'l', 'r': 'u', 'd': 'r', 'l': 'd'}

        def stepSequence(steps: int, direction: str, x: int, y: int):
            step_seq = []
            for _ in range(steps):
                if direction == 'u':
                    y += 1
                elif direction == 'd':
                    y -= 1
                elif direction == 'l':
                    x -= 1
                elif direction == 'r':
                    x += 1
                step_seq.append((x, y))
            return step_seq

        obst = set()
        for o in obstacles:
            obst.add((o[0], o[1]))

        sd, sx, sy, ed = 'u', 0, 0, float('-inf')
        for com in commands:
            if com == -2:
                sd = lt[sd]
            elif com == -1:
                sd = rt[sd]
            else:
                ss = stepSequence(com, sd, sx, sy)
                for s in ss:
                    if s in obst:
                        break
                    sx, sy = s[0], s[1]
                ed = max(ed, sx**2 + sy**2)
        return ed


assert Solution().robotSim(commands=[4, -1, 3], obstacles=[]) == 25
assert Solution().robotSim(
    commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]) == 65
print('Tests Passed!!')
