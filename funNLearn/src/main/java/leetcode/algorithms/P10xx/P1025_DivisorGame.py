"""
    Tag: integer, math, game

    Alice and Bob take turns playing a game, with Alice starting first.
    Initially, there is a number N on the chalkboard.  
    On each player's turn, that player makes a move consisting of:
    -  Choosing any x with 0 < x < N and N % x == 0.
    -  Replacing the number N on the chalkboard with N - x.

    Also, if a player cannot make a move, they lose the game.
    Return True if and only if Alice wins the game, assuming both 
    players play optimally.

    Example 1: Input: 2 Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.

    Example 2: Input: 3 Output: false
    Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

    Note: 1 <= N <= 1000

    Approach:
    -  If N is even, can win.
    -  If N is odd, will lose.

    -  Recursive Prove （Top-down)
        If N is even.
        We can choose x = 1.
        The opponent will get N - 1, which is a odd.
        Reduce to the case odd and he will lose.

        If N is odd,
        2.1 If N = 1, lose directly.
        2.2 We have to choose an odd x.
        The opponent will get N - x, which is a even.
        Reduce to the case even and he will win.

        So the N will change odd and even alternatively until N = 1.

    -  Mathematical Induction Prove （Bottom-up)
        N = 1, lose directly
        N = 2, will win choosing x = 1.
        N = 3, must lose choosing x = 1.
        N = 4, will win choosing x = 1.
"""
from typing import List


class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


assert Solution().divisorGame(2)
assert not Solution().divisorGame(3)
print('Tests Passed!!')
