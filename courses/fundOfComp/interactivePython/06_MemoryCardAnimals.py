# implementation of card game - Memory

import simplegui
import random
import math

WIDTH=600
HEIGHT=600
MAX_PAIRS=50

image_pairs=8
images=image_pairs*2
image_per_ln=int(math.ceil(math.sqrt(images)))
image_sz=WIDTH // image_per_ln

clicks=0
paired=True # dont hide cards when not revealed yet
time=0
# matched image_list blank_image set in new_game()
# image_list is a image ptr + exposed boolean
# first_card second_card set in mouseclick

# helper function to initialize globals
def new_game():
    global clicks, image_list, blank_image, time
    global paired, images, image_per_ln, image_sz, matched
    clicks=0
    images=image_pairs*2
    image_per_ln=int(math.ceil(math.sqrt(images)))
    image_sz=WIDTH // image_per_ln
    matched=True # dont hide cards when nothing revealed yet
    blank_image=simplegui.load_image("http://www.banjo.me.uk/blank.png")
    image_list=[ [simplegui.load_image("http://www.banjo.me.uk/animal"+str(i)+".png"),
                  False] for i in range(image_pairs)]
    image_list.extend(list(image_list[i]) for i in range(image_pairs))
    random.shuffle(image_list)
    time=0
    matched=0
    timer.stop()
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global first_card, second_card, clicks, matched, paired
    new_card=pos[0]//image_sz+image_per_ln*(pos[1]//image_sz)
    if new_card<images:
        timer.start()
        if not image_list[new_card][1]:
            # dont need to use tri-state variable as suggested by
            # the lecturer. Just count if we are half or full way
            # through a turn, and if the last turn was a match.
            if clicks % 2:
                paired=image_list[new_card][0]==image_list[first_card][0]
                second_card=new_card
                image_list[second_card][1]=True
                if paired:
                    matched += 1
                    if matched == image_pairs:
                        timer.stop()
            else:
                if not paired:
                    image_list[first_card][1]=False
                    image_list[second_card][1]=False
                first_card=new_card
                image_list[first_card][1]=True
            clicks += 1       

def new_size(input_str):
    global image_pairs
    input_num=int(input_str)
    if input_num>0 and input_num<=MAX_PAIRS:
        image_pairs=input_num
        new_game()
        error_label.set_text("")
    else:
        error_label.set_text("Only have 50 images, enter 1-50")

def tick():
    global time
    time += 1
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for y in range(0, images, image_per_ln):
        for x in range(y, y+image_per_ln):
            if x<images:
                if image_list[x][1]:
                    canvas.draw_image(image_list[x][0], (64,64), (128,128), [(x % image_per_ln + 0.5)*image_sz, (y // image_per_ln + 0.5)*image_sz ], [image_sz,image_sz])
                else:
                    canvas.draw_image(blank_image, (64,64), (128,128), [(x % image_per_ln + 0.5)*image_sz, (y // image_per_ln + 0.5)*image_sz ], [image_sz,image_sz])
    turns_label.set_text("Turns = "+str(clicks//2))
    timer_label.set_text("Time: "+str(time/600)+":"+str((time%600)/100)+str((time%100)/10)+"."+str(time%10))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Restart", new_game)
turns_label = frame.add_label("Turns = "+str(clicks//2))
timer_label = frame.add_label("Time: 0:00.0")

frame.add_input("New number of animals:", new_size, 200)
error_label = frame.add_label("")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric