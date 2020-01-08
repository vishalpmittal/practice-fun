"""
    Tag: matrix, game

    On an 8 x 8 chessboard, there is one white rook.  There also 
    may be empty squares, white bishops, and black pawns.  These 
    are given as characters 'R', '.', 'B', and 'p' respectively. 
    Uppercase characters represent white pieces, and lowercase 
    characters represent black pieces.

    The rook moves as in the rules of Chess: it chooses one of 
    four cardinal directions (north, east, west, and south), then 
    moves in that direction until it chooses to stop, reaches the 
    edge of the board, or captures an opposite colored pawn by 
    moving to the same square it occupies.  Also, rooks cannot 
    move into the same square as other friendly bishops.

    Return the number of pawns the rook can capture in one move.

    Example 1:
    Input: [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
    Output: 3
    Explanation: In this example the rook is able to capture all the pawns.

    Example 2:
    Input: [
        [".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
    Output: 0
    Explanation: Bishops are blocking the rook to capture any pawn.

    Example 3: 
    Input: [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
    Output: 3
    Explanation: The rook can capture the pawns at positions b5, d6 and f5.

    Note:
    -  board.length == board[i].length == 8
    -  board[i][j] is either 'R', '.', 'B', or 'p'
    -  There is exactly one cell with board[i][j] == 'R'
"""
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # create string of the arrangement and then find count of pR or Rp in the string
        horizontal = []
        vertical = []
        for i in range(0, 8):
            temp_hor = ''
            temp_ver = ''
            for j in range(0, 8):
                if board[i][j] != '.':
                    temp_hor = temp_hor + board[i][j]
                if board[j][i] != '.':
                    temp_ver = temp_ver + board[j][i]
            horizontal.append(temp_hor)
            vertical.append(temp_ver)
        count = 0
        new = horizontal + vertical
        for i in range(0, len(new)):
            if 'Rp' in str(new[i]):
                count += 1
            if 'pR' in str(new[i]):
                count += 1
        return(count)


assert Solution().numRookCaptures([
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    ["p", "p", ".", "R", ".", "p", "B", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "B", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
]) == 3
print('Tests Passed!!')
