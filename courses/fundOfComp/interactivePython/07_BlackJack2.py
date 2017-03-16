# Mini-project #6 - Blackjack
import simplegui
import random
 
# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
win_msg = ""
player_inst = "Try the game"
d_hand = p_hand = mydeck = None


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self, type = 'player'):
        self.hand = []
        self.type = type

    def __str__(self):
        # return a string representation of a hand
        hand_str = ""
        for c in self.hand:
            hand_str = hand_str + str(c) +','
        return hand_str

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        total = 0
        num_of_aces = 0
        # count aces as 1, 
        for c in self.hand:
            total+=VALUES[c.get_rank()]
            if VALUES[c.get_rank()] ==1:
                num_of_aces +=1
            
        #if the hand has an ace, then add 10 to hand value if it doesn't bust
        if num_of_aces ==1 and total+10 <=21:
            return total+10
        else:
            return total
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas
        i =0
        if self.type=="dealer" and in_play:
            new_pos = (pos[0] +CARD_BACK_CENTER[0], pos[1]+CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, new_pos, CARD_BACK_SIZE)
            self.hand[1].draw(canvas, (pos[0]+CARD_SIZE[0]+20, pos[1])) 
        else:
            for c in self.hand:
               c.draw(canvas, (pos[0]+(i*CARD_SIZE[0]) + (i*20), pos[1])) 
               i += 1
 
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suite in SUITS:
            for rank in RANKS:
                temp_card = Card(suite, rank)
                self.deck.append(temp_card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        deck_str = ""
        for c in self.deck:
            deck_str = deck_str + str(c) +','
        return deck_str

#define event handlers for buttons
def deal():
    global outcome, in_play, player_inst, d_hand, p_hand, mydeck, score
    
    if in_play:
        outcome = "You Lose!!!"
        player_inst = "Deal?"
        score -= 1
        in_play = False 

    mydeck = Deck()
    mydeck.shuffle()
    p_hand = Hand()
    d_hand = Hand("dealer")
    
    p_hand.add_card(mydeck.deal_card())
    p_hand.add_card(mydeck.deal_card())
    d_hand.add_card(mydeck.deal_card())
    d_hand.add_card(mydeck.deal_card())
    in_play = True
    outcome = ""
    player_inst = "Hit or Stand?"

# get one more card from dealer
def hit():
    global in_play, player_inst, p_hand, d_hand, mydeck, score, outcome
    
    # if the hand is in play, hit the player
    if in_play:
        p_hand.add_card(mydeck.deal_card())
        
        # if busted, assign a message to outcome, update in_play and score        
        if p_hand.get_value() > 21:
            outcome = "Player Burst!!!"
            player_inst = "Deal Again?"
            score -= 1
            in_play = False
        
        else:
            player_inst = "Hit or Stand?"
       
# Don't want any more cards from the dealer
def stand():
    global in_play, player_inst, p_hand, d_hand, mydeck, score, outcome

    # if hand is in play
    if in_play:
        #repeatedly hit dealer until his hand has value 17 or more
        while (d_hand.get_value() < 17):
            d_hand.add_card(mydeck.deal_card())
            
        # assign a message to outcome, update in_play and score
        if (d_hand.get_value()>21):
            outcome = "Dealer Burst!!!"            
            player_inst = "Deal Again?"
            score += 1
            in_play = False            
            
        elif p_hand.get_value()>d_hand.get_value():
            outcome = "Dealer Lose!!!"            
            player_inst = "Deal Again?"
            score += 1
            in_play = False            
            
        elif d_hand.get_value() >= p_hand.get_value():
            outcome = "Player Lose!!!"   
            player_inst = "Deal Again?"
            score -= 1
            in_play = False 

def reset():
    global score
    deal()
    score = 0
            
# draw handler    
def draw(canvas):
    global score, player_inst, d_hand, p_hand, CARD_BACK_SIZE, CARD_BACK_CENTER, card_back, outcome
    
    # Draw the basic components on the UI
    canvas.draw_text('BlackJack', (20, 50), 45, 'Black')
    canvas.draw_line([5, 55], [590, 55], 5, 'Black')
    
    canvas.draw_text('Dealer', (40, 105), 35, 'Gray')
    canvas.draw_polygon([(40, 110), (40, 270), (550, 270), (550, 110)], 1, 'Black', 'Silver')
    
    canvas.draw_text('Player', (40, 340), 35, 'Blue')
    canvas.draw_text('Score: '+ str(score), (400, 340), 35, 'Blue')
    canvas.draw_polygon([(40, 350), (40, 510), (550, 510), (550, 350)], 1, 'Black', 'Blue')

    canvas.draw_text(outcome, (120, 550), 30, 'Maroon')    
    canvas.draw_text(player_inst, (350, 550), 30, 'Maroon')    
    
    d_hand.draw(canvas, (80, 135))
    p_hand.draw(canvas, (80, 370))

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_label(' ')
frame.add_button("Hit",  hit, 200)
frame.add_label(' ')
frame.add_button("Stand", stand, 200) 
for x in range(0, 20):
    frame.add_label(' ')
frame.add_label('---------------------------------------')
frame.add_button("Reset Game", reset, 200) 

frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
