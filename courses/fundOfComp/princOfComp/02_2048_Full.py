"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def get_random_2048_digit():
    """
    Returns 2 or 4 randomly with 90%  probablity of returning 2
    """
    random_num_list = [2]*9
    random_num_list.append(4)
    return random.choice(random_num_list)

def slide_zeros_to_right(raw_list):
    """ Function to move all the zeros to 
    right most in a list """
    for iter_out in range(0, len(raw_list)-1):
        for iter_in in range(0, len(raw_list)-iter_out-1):
            if(raw_list[iter_in] == 0 and raw_list[iter_in+1]!=0):
                raw_list[iter_in] = raw_list[iter_in+1]
                raw_list[iter_in+1] = 0

def add_left_common_elements(add_list):
    """ Fuction that takes a list and starting from 
    left adds the similar digits"""
    index = 0
    curr_digit = 0
    while (index < len(add_list)-1):
        if (add_list[index] != 0):
            curr_digit = add_list[index]
            # if duplicate numbers found, add and move two places
            if(curr_digit == add_list[index+1]):
                add_list[index] *= 2
                add_list[index+1] = 0
                curr_digit = 0 
                index += 2
            # else move one place
            else:
                index += 1
        # encountered zero move one place
        else:
            index += 1

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    merged_line = list(line)
    slide_zeros_to_right(merged_line)
    add_left_common_elements(merged_line)
    slide_zeros_to_right(merged_line)
    return merged_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Construct the game class
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        print "Reset Grid"
        self._grid = [[0*col*row for col in range(self.get_grid_width())]
                           for row in range(self.get_grid_height())]

        rand_tile = self.get_radom_empty_tile_loc() 
        rand_value = get_random_2048_digit()
        self.set_tile(rand_tile[0], rand_tile[1], rand_value)
        
        rand_tile2 = self.get_radom_empty_tile_loc()
        # get a new random tile untill random returns different tiles
        while(rand_tile2==rand_tile):
            rand_tile2 = self.get_radom_empty_tile_loc()
        rand_value2 = get_random_2048_digit()
        self.set_tile(rand_tile2[0], rand_tile2[1], rand_value2)

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = '[' + '\n '.join(str(p) for p in self._grid) +']'
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_grid = str(self)
        
        if direction == UP:
            for trav_col in range(self.get_grid_width()):
                self.traverse_and_merge((0, trav_col), OFFSETS[UP], self.get_grid_height())

        elif direction == DOWN:
            for trav_col in range(self.get_grid_width()):
                self.traverse_and_merge((self.get_grid_height()-1 , trav_col), OFFSETS[DOWN], self.get_grid_height())
                
        elif direction == RIGHT:
            for trav_row in range(self.get_grid_width()):
                self.traverse_and_merge((trav_row , self.get_grid_width()-1), OFFSETS[RIGHT], self.get_grid_width())
            
        elif direction == LEFT:
            for trav_row in range(self.get_grid_width()):
                self.traverse_and_merge((trav_row , 0), OFFSETS[LEFT], self.get_grid_width())

        else:
            print ("Wrong movement direction")
        
        moved_grid = str(self)
        if (initial_grid != moved_grid):
            print "Tiles Moved, Adding a new random tile"
            self.new_tile()
        else:
            print "No Movement: No random tile added"

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile_value = get_random_2048_digit()
        random_empty_tile = self.get_radom_empty_tile_loc()
        if random_empty_tile is not None:
            self.set_tile(random_empty_tile[0], random_empty_tile[1], tile_value)

    def set_tile(self, s_row, s_col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[s_row][s_col] = value

    def get_tile(self, g_row, g_col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[g_row][g_col]
    
    def get_radom_empty_tile_loc(self):
        """
        Return a random location in the grid with value as zero
        """
        empty_tile_list = []
        for rand_row in range (self.get_grid_height()):
            for rand_col in range (self.get_grid_width()):
                if (self._grid[rand_row][rand_col] == 0):
                    tile_tuple = (rand_row, rand_col)
                    empty_tile_list.append(tile_tuple)
        
        if not empty_tile_list:
            print "No empty tiles remining"
            return None
        else:
            return random.choice(empty_tile_list)
    
    def traverse_and_merge(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction
    
        Start_cell is a tuple(row, col) denoting the starting cell
    
        direction is a tuple that contains difference between 
        consecutive cells in the traversal
        
        This function returns a list corresponding to the travering order
        """
        merge_list=[]
        for get_step in range(num_steps):
            get_row = start_cell[0] + get_step * direction[0]
            get_col = start_cell[1] + get_step * direction[1]
            if get_row < self.get_grid_height() and get_col < self.get_grid_width():
                merge_list.append(self._grid[get_row][get_col])
        
        merged_list = merge(merge_list)
        
        list_traverse = 0
        for set_step in range(num_steps):
            set_row = start_cell[0] + set_step * direction[0]
            set_col = start_cell[1] + set_step * direction[1]
            if get_row < self.get_grid_height() and get_col < self.get_grid_width():
                self._grid[set_row][set_col] = merged_list[list_traverse]
                list_traverse += 1

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
