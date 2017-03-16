"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(120)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    curr_result = board.check_win()
    if curr_result != None:
        return SCORES[curr_result], (-1, -1)
    
    empty_squares = board.get_empty_squares()
    
    max_till_now = -10
    min_till_now = 10
    ret_square = (-1, -1)
    
    for square in empty_squares:
        rec_board = board.clone()
        rec_board.move(square[0], square[1], player)
        curr_return = mm_move(rec_board, provided.switch_player(player))
        curr_score = curr_return[0]
        
        if player == provided.PLAYERX:
            if curr_score == 1:
                max_till_now = 1
                ret_square = square
                break
            if curr_score > max_till_now:
                max_till_now = curr_score
                ret_square = square
            
        elif player == provided.PLAYERO:
            if curr_score == -1:
                min_till_now = -1
                ret_square = square
                break
            if curr_score < min_till_now:
                min_till_now = curr_score
                ret_square = square
    
    if player == provided.PLAYERX:
        return max_till_now, ret_square
    elif player == provided.PLAYERO:
        return min_till_now, ret_square

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    print move
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
