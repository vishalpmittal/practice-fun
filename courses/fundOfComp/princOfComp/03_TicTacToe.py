"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 50         # Number of trials to run
SCORE_CURRENT = 5.0 # Score for squares played by the current player
SCORE_OTHER = 5.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    board: current board 
    player: next player to move
    function: play a game:
            start with the given player, 
            make random moves, 
            alternate between players, 
            return when game is over
    return: nothing
    """
    empty_sqs = board.get_empty_squares()
    curr_player = player
    while((len(empty_sqs)!=0) and (board.check_win() is None)):
        next_move = random.choice(empty_sqs)
        board.move(next_move[0], next_move[1], curr_player)
        curr_player = provided.switch_player(curr_player)
        empty_sqs = board.get_empty_squares()
    return

def mc_update_scores(scores, board, player):
    """
    scores: grid of scores, (list of lists), same dimention as ttt board
    board: completed game board
    player: machine player
    function: score the completed board and update the scroes grid
    return: nothing
    """
    # if board is not complete or a draw just return
    if((board.check_win() is None) or (board.check_win() == provided.DRAW)):
        return

    for row_num in range(0, board.get_dim()):
        for col_num in range(0, board.get_dim()):
            appender = 0        
            curr_square=board.square(row_num, col_num)

            if(board.check_win() == player):
                # add SCORE_CURRENT to player square score
                if curr_square == player:
                    appender += SCORE_CURRENT
                # Minus SCORE_OTHER to other square score
                elif curr_square==provided.switch_player(player):
                    appender -= SCORE_OTHER

            elif(board.check_win() == provided.switch_player(player)):
                # Minus SCORE_CURRENT to Player square score
                if curr_square == player:
                    appender -= SCORE_CURRENT
                # add SCORE_OTHER to other square score
                elif curr_square==provided.switch_player(player):
                    appender += SCORE_OTHER
            
            scores[row_num][col_num] += appender

def get_best_move(board, scores):
    """
    board: current board
    scores: 
    function: find all empty squares with maximum score, randomly return
    return: random one the empty squares 
            return none if board is full 
    """
    high_score = -1000
    for row_num in range(0, board.get_dim()):
        for col_num in range(0, board.get_dim()):
            if ((scores[row_num][col_num] > high_score) and
               (board.square(row_num, col_num)==provided.EMPTY)):
                high_score = scores[row_num][col_num]
    
    high_sqr_list = []
    for row_num in range(0, board.get_dim()):
        for col_num in range(0, board.get_dim()):
            if ((scores[row_num][col_num]==high_score) and 
                (board.square(row_num, col_num)==provided.EMPTY)):
                high_sqr_list.append((row_num, col_num))
    
    if(len(high_sqr_list)==0):
        return None
    else:
        return random.choice(high_sqr_list)

def mc_move(board, player, trials):
    """
    board: current board
    player: machine player
    trials: number of trials to run
    funtion: use other functions you have written
            use monte carlo simulation
    return: a move for the machine player in the form of a (row, column) tuple
    """
    scores = [[0*col*row for col in range(board.get_dim())] 
              for row in range(board.get_dim())]
    
    for trial_num in range(trials):
        print str(trial_num)
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)
    
    best_move=get_best_move(board, scores)
    return best_move

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.
#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
