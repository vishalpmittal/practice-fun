"""
    tag: math, game

    Have the function  BlackjackHighest(strArr) take the strArr parameter being passed which will 
    be an array of numbers and letters representing blackjack cards. Numbers in the array will 
    be written out. So for example strArr may be ["two","three","ace","king"]. The full list 
    of possibilities for strArr is: two, three, four, five, six, seven, eight, nine, ten, 
    jack, queen, king, ace. 

    Your program should output below, above, or blackjack signifying if you have blackjack 
    (numbers add up to 21) or not and the highest card in your hand in relation to whether 
    or not you have blackjack. If the array contains an ace but your hand will go above 21, 
    you must count the ace as a 1. You must always try and stay below the 21 mark. So using 
    the array mentioned above, the output should be below king. The ace is counted as a 1 in 
    this example because if it wasn't you would be above the 21 mark. Another example would 
    be if strArr was ["four","ten","king"], the output here should be above king. If you have 
    a tie between a ten and a face card in your hand, return the face card as the 
    "highest card". If you have multiple face cards, the order of importance is jack, queen, king. 
"""

rank_value = {
  'two': 2, 'three':3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
  'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 1
}

def BlackjackHighest(strArr):
  total = 0
  return_str = ''
  aces = 0
  highest_points = -1
  highest_rank = -1

  # first calculate the hand value with ace value as 1 and count number of aces too
  for rank in strArr:
    if rank == 'ace':
      aces += 1
    total += rank_value[rank]
    if highest_points < rank_value[rank]:
      highest_points = rank_value[rank]
      highest_rank = rank
  
  # if total < 11 then ace value can be changed to 11, so add 10 to value and reduce number of aces
  ace_margin = 21 - total 
  if ace_margin >= 10 and aces > 0:
    total += 10
    aces -= 1
    highest_rank = 'ace'

  if total == 21:
    return_str += 'blackjack'
  elif total < 21:
    return_str += 'below'
  elif total > 21:
    return_str += 'above'
  
  # return total  
  return return_str + ' ' + str(highest_rank)

assert(str(BlackjackHighest(["four","ace","ten"]) == 'below ten'))      # 15
assert(str(BlackjackHighest(["ace", "queen"]) == 'blackjack ace'))      # 21
assert(str(BlackjackHighest(["ace","ace","queen"]) == 'below queen'))   # 12

print("Tests Passed!")
