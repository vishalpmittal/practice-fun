# implementation of card game - Memory
import simplegui
import random 
NUM_LIST=[]
LIST_STATE= [0]*16
GAME_STATE = TURNS=0
EXPO_CARD1=EXPO_CARD2=-1

# helper function to initialize globals
def new_game():
    global NUM_LIST, LIST_STATE, TURNS
    NUM_LIST = range(8) + range(8)    
    random.shuffle(NUM_LIST)
    TURNS = 0
    label.set_text("Turns = "+ str(TURNS))
    LIST_STATE= [0]*16

# define event handlers
def mouseclick(pos):
    global NUM_LIST, LIST_STATE, TURNS, GAME_STATE, EXPO_CARD1, EXPO_CARD2
    card_n = int(pos[0]/50)
    if(LIST_STATE[card_n] == 0):
        if GAME_STATE == 0:
            EXPO_CARD1 = card_n
            LIST_STATE[EXPO_CARD1]=1
            GAME_STATE=1
            TURNS += 1
        elif GAME_STATE == 1:
            EXPO_CARD2=card_n
            LIST_STATE[EXPO_CARD2]=1
            if NUM_LIST[EXPO_CARD1]==NUM_LIST[EXPO_CARD2]:
                LIST_STATE[EXPO_CARD1] = LIST_STATE[EXPO_CARD2] = 2
                GAME_STATE=0
            else:
                GAME_STATE=2
        elif GAME_STATE == 2:
            LIST_STATE[EXPO_CARD1] = LIST_STATE[EXPO_CARD2]=0
            EXPO_CARD1 = card_n
            LIST_STATE[EXPO_CARD1]=1
            GAME_STATE=1  
            TURNS += 1
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global NUM_LIST, LIST_STATE
    label.set_text("Turns = "+ str(TURNS))    
    for n in range(16):
        canvas.draw_line((n*50, 0), (n*50, 100), 2, 'Red')
        if LIST_STATE[n]==0:
            canvas.draw_polygon([[(n*50)+2, 0], [(n*50)+2, 100], [((n+1)*50)-2, 100], [((n+1)*50)-2, 0]], 2, 'Green', 'Green')
        else:
            canvas.draw_text(str(NUM_LIST[n]), ((n*50)+15, 60), 40, 'Red')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(TURNS))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()