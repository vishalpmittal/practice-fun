"""
    tag: list, array

    Eight house, represented as cells, are arranged in a straight line. 
    Each day every cell competes with its adjacent cells (neighbors). 
    An integer value of 1 represents an active cell and a value of 0 represents 
    an inactive cell. If the neighbors on both the sides of a cell are either 
    active or inactive, the cell becomes inactive on the next day, 
    otherwise the cell becomes active. 
    
    The two cells on each end havea single adjacent cell, so assume that 
    the unoccupied space opposite side is an inactive cell. Even after updating 
    the cell state, consider its previous state when updating the state of other 
    cells. The state information of all cells should be updated simultaneously. 

    Write an algorithm to output the state of the cells after the given number
    of days. 
    
    Input
    state:- a list of integers representing the current state of cells day, 
    an integer representing the number of days. 

    output Return a list of integers representing the state of the cells after
    given number of days. 
    
    Note:
    The elements of the list states contains Os and Is only. 
"""


def cellCompete(states, days):
    states = [0] + states + [0]

    for _ in range(days):
        prev_cell_state = 0
        for cell in range(1, len(states) - 1):
            curr_cell_prev_state = states[cell]
            if prev_cell_state + states[cell + 1] in [0, 2]:
                states[cell] = 0
            else:
                states[cell] = 1
            prev_cell_state = curr_cell_prev_state

    return states[1 : len(states) - 1]

