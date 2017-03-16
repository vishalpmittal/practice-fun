# Rock-paper-scissors-lizard-Spock random guess program

# Program rules :
# Scissors cut paper
# Paper covers rock
# Rock crushes lizard
# Lizard poisons Spock
# Spock smashes scissors
# Scissors decapitate lizard
# Lizard eats paper
# Paper disproves Spock
# Spock vaporizes rock
# Rock crushes scissors

import random

# helper functions
def number_to_name(number):
    """
    Return respective name for number
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return None
    
def name_to_number(name):
    """
    Return respective number for name
    """
    if name == 'rock':
        return 0
    elif name =='Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return None
    
def rpsls(name): 
    # convert name to player_number
    player_number = name_to_number(name)
    
    # compute random guess for comp_number
    comp_number = random.randrange(0, 5)
    
    # compute difference of player_number and comp_number modulo five
    guess_diff = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner
    if guess_diff == 0:
        winner_str = 'Player and computer tie!'
    elif guess_diff == 1 or guess_diff == 2:
        winner_str = 'Computer wins!'
    elif guess_diff == 3 or guess_diff == 4:
        winner_str = 'Player wins!'
 
    # print results
    print "Player chooses %s" % name
    print "Computer chooses %s" % number_to_name(comp_number)
    print "%s \n" % winner_str

# Tests
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
