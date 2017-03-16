"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
            
    def __str__(self):
        ans_str = poc_grid.Grid.__str__(self)
        ans_str += "\n Zombie List: " + str(self._zombie_list)
        ans_str += "\n Human List: " + str(self._human_list)
        return ans_str
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._human_list = []
        self._zombie_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for dummy_zombie in self._zombie_list:
            yield dummy_zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for dummy_human in self._human_list:
            yield dummy_human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(self.get_grid_height(), self.get_grid_width())
        visited.clear()
        
        grid_prod = self.get_grid_width() * self.get_grid_height()
        distance_field = [[grid_prod for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]

        boundary = poc_queue.Queue()
        if (entity_type == ZOMBIE):
            for zombie in self.zombies():
                boundary.enqueue(zombie)
        
        elif (entity_type == HUMAN):
            for human in self.humans():
                boundary.enqueue(human)
        
        for que_element in boundary:
            visited.set_full(que_element[0], que_element[1])
            distance_field[que_element[0]][que_element[1]]=0

        while(len(boundary)>0):
            current_cell = boundary.dequeue()
            all_four_neighbor = visited.four_neighbors(current_cell[0], current_cell[1])
            for neighbor_cell in all_four_neighbor:
                if (visited.is_empty(neighbor_cell[0], neighbor_cell[1])):
                    if (self.is_empty(neighbor_cell[0], neighbor_cell[1])):
                        visited.set_full(neighbor_cell[0], neighbor_cell[1])
                        boundary.enqueue((neighbor_cell[0], neighbor_cell[1]))
                        distance_field[neighbor_cell[0]][neighbor_cell[1]]=distance_field[current_cell[0]][current_cell[1]] + 1
        
        return distance_field
        
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_human_list = []
        
        # for each human in the human list
        for human in self.humans():
            possible_moves = self.eight_neighbors(human[0], human[1])
            
            move_list = []
            longest_dist = 1
            
            # For each neighbor out of eight
            for poss_move in possible_moves:
                # continue to next if obstacle, zombie or new human already present
                if not self.is_empty(poss_move[0], poss_move[1]) or poss_move in move_list or poss_move in self._zombie_list:
                    continue

                distance = zombie_distance_field[poss_move[0]][poss_move[1]]
                
                if distance == longest_dist:
                    move_list.append(poss_move)
                elif distance > longest_dist:
                    move_list = []
                    move_list.append(poss_move)
                    longest_dist = distance
            
            if len(move_list) > 0:
                new_human_list.append(random.choice(move_list))        
            else:
                new_human_list.append(human)
        
        self._human_list = new_human_list
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombie_list = []
        
        for zombie in self.zombies():
            if zombie in self._human_list:
                new_zombie_list.append(zombie)
                continue
            
            possible_moves = self.four_neighbors(zombie[0], zombie[1])
            
            move_list = []
            shortest_dist = 10000000000000
            
            for poss_move in possible_moves:
                if not self.is_empty(poss_move[0], poss_move[1]) or poss_move in new_zombie_list:
                    continue
                distance = human_distance_field[poss_move[0]][poss_move[1]]
                if distance == shortest_dist:
                    move_list.append(poss_move)
                elif distance < shortest_dist:
                    move_list = []
                    move_list.append(poss_move)
                    shortest_dist = distance
                
            if len(move_list) > 0:
                new_zombie_list.append(random.choice(move_list))
            else:
                new_zombie_list.append(zombie)
            
        self._zombie_list = new_zombie_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
