"""
Loyd's Fifteen puzzle (solver and visualizer)
note that solved configuration has the blank (zero) tile in upper left;
use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    class representation for The Fifteen Puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        initialize puzzle with default height and width;
        returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        generate string representation for puzzle;
        returns a string
        """
        ans = ''
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += '\n'
        return ans

    ########################################################
    # GUI methods

    def get_height(self):
        """
        getter for puzzle height; returns an integer
        """
        return self._height

    def get_width(self):
        """
        getter for puzzle width; returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        getter for the number at tile position pos; returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        make a copy of the puzzle to update during solving;
        returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # core puzzle methods
    def current_position(self, solved_row, solved_col):
        """
        locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved;
        returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, 'Value ' + str(solved_value) + ' not found'

    def update_puzzle(self, move_string):
        """
        updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == 'l':
                assert zero_col > 0, 'move off grid: ' + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == 'r':
                assert zero_col < self._width - 1, 'move off grid: ' + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == 'u':
                assert zero_row > 0, 'move off grid: ' + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == 'd':
                assert zero_row < self._height - 1, 'move off grid: ' + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, 'invalid direction: ' + direction

    ########################################################
    # phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1);
        returns a boolean
        """
        # 0 tile is positioned at (i, j) as expected
        if self.get_number(target_row, target_col) == 0:
            # all tiles in row i to the right of position (i, j) are solved
            for columns in range(target_col + 1, self.get_width()):
                if not (target_row, columns) == self.current_position(target_row, columns):
                    return False
            # all tiles in rows i + 1 or below are positioned at their solved location
            # if 0 tile is in last row, no need to check for more
            if not target_row + 1 == self.get_height():
                for columns_bellow in range(0, self.get_width()):
                    if not (target_row + 1, columns_bellow) == self.current_position(target_row + 1, columns_bellow):
                        return False
            return True

        return False

    def helper_move(self, target_row, target_col, curr_row, curr_col):
        """
        helper function to move internal tile
        prereq : (k < i) or on the same row to the left (i = k and l < j);
        return: a move string
        """
        move_str = ''
        col_change = target_col - curr_col
        row_change = target_row - curr_row
        move_str += row_change * 'u'

        if col_change == 0:
            move_str += 'ld' + (row_change - 1) * 'druld'
        else:
            if col_change > 0:
                move_str += col_change * 'l'
                if curr_row == 0:
                    move_str += (abs(col_change) - 1) * 'drrul'
                else:
                    move_str += (abs(col_change) - 1) * 'urrdl'
            elif col_change < 0:
                move_str += (abs(col_change) - 1)  * 'r'
                if curr_row == 0:
                    move_str += abs(col_change) * 'rdllu'
                else:
                    move_str += abs(col_change) * 'rulld'
            move_str += row_change * 'druld'
        return move_str
            

    def solve_interior_tile(self, target_row, target_col):
        """
        makes use of helper function move()
        updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col)
        curr_pos = self.current_position(target_row, target_col)
        move_str = self.helper_move(target_row, target_col, curr_pos[0], curr_pos[1])
        self.update_puzzle(move_str)
        assert self.lower_row_invariant(target_row, target_col - 1)
        return move_str
       
    def solve_col0_tile(self, target_row):
        """
        solve tile in column zero on specified row (> 1);
        updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0)
        move_str = 'ur'       
        self.update_puzzle(move_str)

        curr_pos = self.current_position(target_row, 0)
        # target tile already in place
        if curr_pos[0] == target_row and curr_pos[1] == 0:
            tmp_move_str = (self.get_width() - 2) * 'r'
            self.update_puzzle(tmp_move_str)
            move_str += tmp_move_str
        else:
            tmp_move_str = self.helper_move(target_row - 1, 1, curr_pos[0], curr_pos[1])
            tmp_move_str += 'ruldrdlurdluurddlu' + (self.get_width() - 1) * 'r'
            self.update_puzzle(tmp_move_str)
            move_str += tmp_move_str
        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
        return move_str

    ########################################################
    # phase two methods

    def row0_invariant(self, target_col):
        """
        check whether the puzzle satisfies the row zero invariant at the given column (col > 1);
        returns a boolean
        """
        if not self.get_number(0, target_col) == 0:
            return False

        for column in range(self.get_width()):
            for row in range(self.get_height()):
                if (row == 0 and column > target_col) or (row == 1 and column >= target_col) or row > 1:
                    if not (row, column) == self.current_position(row, column):
                        return False
                    
        return True
    
    def row1_invariant(self, target_col):
        """
        check whether the puzzle satisfies the row one invariant at the given column (col > 1);
        returns a boolean
        """
        if not self.lower_row_invariant(1, target_col):
            return False

        for column in range(0, self.get_width()):
            for row in range(2, self.get_height()):
                if not (row, column) == self.current_position(row, column):
                    return False

        return True
    
    def solve_row0_tile(self, target_col):
        """
        solve the tile in row zero at the specified column;
        updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col)
        move_str = 'ld'       
        self.update_puzzle(move_str)
        curr_pos = self.current_position(0, target_col)

        if curr_pos[0] == 0 and curr_pos[1] == target_col:
            return move_str
        else:
            tmp_move_str = self.helper_move(1, target_col - 1, curr_pos[0], curr_pos[1])
            tmp_move_str += "urdlurrdluldrruld"
            self.update_puzzle(tmp_move_str)
            move_str += tmp_move_str

        return move_str

    def solve_row1_tile(self, target_col):
        """
        solve the tile in row one at the specified column;
        updates puzzle and returns a move string
        """
        curr_pos = self.current_position(1, target_col)
        move_str = self.helper_move(1, target_col, curr_pos[0], curr_pos[1])
        move_str += 'ur'
        self.update_puzzle(move_str)

        return move_str
    
    ########################################################
    # phase 3 methods
    def solve_2x2(self):
        """
        solves the upper left 2x2 part of the puzzle;
        doesn't check for insolvable configuration!,
        updates the puzzle and returns a move string
        """
        move_str = ''
        mini_move_str = ''
              
        if self.get_number(1, 1) == 0:
            mini_move_str += 'ul'
            self.update_puzzle(mini_move_str)
            if (0, 1) == self.current_position(0, 1) and (1, 1) == self.current_position(1, 1):
                return mini_move_str

            if self.get_number(0, 1) < self.get_number(1, 0):
                move_str += 'rdlu'
            else:
                move_str += 'drul'        
            self.update_puzzle(move_str)
            
        return mini_move_str + move_str


    def solve_puzzle(self):
        """
        generate a solution string for a puzzle;
        updates the puzzle and returns a move string
        """
        move_str = ''

        row_anchor = self.get_height() - 1
        col_anchor = self.get_width() - 1

        row_current, column_current = self.current_position(0, 0)

        col_change = column_current - col_anchor
        row_change = row_current - row_anchor

        tmp_move_str = abs(col_change) * 'r' + abs(row_change) * 'd'
        self.update_puzzle(tmp_move_str)
        move_str += tmp_move_str

        # solve all bottom but 2 rows from right to left
        for row in range(row_anchor, 1, -1):
            for column in range(col_anchor, 0, -1):
                move_str += self.solve_interior_tile(row, column)
            move_str += self.solve_col0_tile(row)

        # solve all but two columns of the top two rows
        for column in range(col_anchor, 1, -1):
            move_str += self.solve_row1_tile(column)
            move_str += self.solve_row0_tile(column)

        # solve the 2 X 2 portion remaining
        move_str += self.solve_2x2()
        return move_str

########################################################
# start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

