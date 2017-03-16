# Mini Project "Guess the number"

# Import required libraries
import simplegui
import random
import math

# Global variables Used
num_base = 0
num_range = 100
secret_num = 0
guess_count = 7

def new_game():
    """ Start or restart the game. 
        Guess a new number. 
        Compute and reset the guess count. """
    global secret_num
    global guess_count
    secret_num = random.randrange(num_base, num_range)
    
    # Compute the guess count based on number range
    compute_num = num_range - num_base +1
    for x in range(num_base, num_range):
        if (2**x) >= compute_num:
            guess_count = x
            break
            
    # Print new game message
    print "New game. Range is from " + str(num_base) + " to " + str(num_range)
    print "Number of remaining guesses is " + str(guess_count) + "\n"

def range100():
    """ Change the range to [0, 100) and start new game. """
    global num_range
    num_range = 100
    new_game()

def range1000():
    """ Change the range to [0, 1000) and start new game. """
    global num_range
    num_range = 1000  
    new_game()
    
def input_guess(guess):
    """ Get the user guess and compare to secret number.
        If matach print correct and start a new game.
        If out of guesses start a new game. """
    global secret_num
    global guess_count
    user_guess = int(guess)
    
    guess_count -= 1
    print "Guess was " + str(user_guess)
    print "Number of remaining guesses is " + str(guess_count)
    if user_guess == secret_num:
        print "Correct!\n"
        new_game()
        return
    elif user_guess < secret_num:
        print "Higher!\n"
    elif user_guess > secret_num:
        print "Lower!\n"
    
    if guess_count <= 0:
        print "Out of guesses!!! You lose!!! "
        print "Secret Number was "+ str(secret_num) + "\n"
        new_game()

# create GUI frame
gn_frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
gn_frame.add_button("Range is [0, 100)", range100, 200)
gn_frame.add_button("Range is [0, 1000)", range1000, 200)
gn_frame.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()
gn_frame.start()
