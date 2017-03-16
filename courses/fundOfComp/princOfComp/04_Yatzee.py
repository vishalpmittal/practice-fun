"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, 
only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(40)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    high_score=-1
    operated_digits = []
    
    for out_indx in range (len(hand)):
        digit_sum=0
        # Skip if already operated on it
        if (hand[out_indx] in operated_digits):
            continue
        operated_digits.append(hand[out_indx])

        # Calculate the total sum of digits
        for inr_indx in range (out_indx, (len(hand))):
            if hand[inr_indx] != hand[out_indx]:
                break
            digit_sum+=hand[out_indx]

        # Compare with overall and change if needed
        if high_score<digit_sum:
            high_score = digit_sum

    return high_score

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    # get all the outcomes from free dices
    outcomes = []
    for possible_out in range(1, num_die_sides+1):
        outcomes.append(possible_out)
    outcomes = tuple(outcomes)
    all_free_seq = gen_all_sequences(outcomes, num_free_dice)

    # For each free seq, create full seq, sort and calculate score
    all_seq_score = []
    for free_seq in all_free_seq:
        full_seq = list(held_dice + free_seq)
        full_seq.sort()
        seq_score = score(tuple(full_seq))     
        all_seq_score.append(seq_score)
    
    # get the average of all the possible scores
    total_sum = 0
    for seq_sum in all_seq_score:
        total_sum += seq_sum
    
    average_sum = float(total_sum) / float(len(all_seq_score))
    return average_sum

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    powerset = set()
    powerset.add(())
    for sset_len in range(1, len(hand)+1):
        len_ss_list = gen_subsets(hand, sset_len)
        for len_ss in len_ss_list:
            len_ss.sort()
            tmp_tuple = tuple(len_ss)
            powerset.add(tmp_tuple)
    return powerset

def gen_subsets(ss_list, length):
    """
    Generates subsets of particular length
    returns a list of lists (subsets)
    """
    if length == 0:
        return [[]]
    if len(ss_list) == 0:
        return []
    rec_list = ss_list[1:]
    subsets = gen_subsets(rec_list, length-1)
    for element in subsets:
        element.append(ss_list[0])
    return subsets+gen_subsets(rec_list, length)

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    (expected_score, (hold_dice))
    """
    # Get all the hold possible
    all_holds_set = gen_all_holds(hand)
    print all_holds_set
    
    strategic_score = float(-1)
    strategic_hold = ()

    # For each hold get the average value
    for hold_set in all_holds_set:
        free_dice_to_roll = len(hand)-len(hold_set)
        ave_exp_val = expected_value(hold_set, num_die_sides, free_dice_to_roll)
        
        # if Average value is higher than strategic_score, swap
        if strategic_score < ave_exp_val:
            strategic_score = ave_exp_val
            strategic_hold = hold_set

    return (strategic_score, strategic_hold)

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
  
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)

