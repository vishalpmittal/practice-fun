# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       

BALL_RADIUS = 20
ball_acc = 1.3

PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

lpad_centre=HEIGHT/2
rpad_centre=HEIGHT/2
lpad_vel=0
rpad_vel=0
pad_acc=4

lscore = 0
rscore = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == 'left':
        ball_vel = [(-(random.randrange(110, 150)))/(random.randrange(60, 100)), (-(random.randrange(110, 150)))/(random.randrange(60, 100))]
    else:
        ball_vel = [((random.randrange(110, 150)))/(random.randrange(60, 100)), (-(random.randrange(110, 150)))/(random.randrange(60, 100))]
    
# define event handlers
def new_game():
    global lpad_vel, rpad_vel, lpad_centre, rpad_centre
    global lscore, rscore
    lscore = 0
    rscore = 0
    lpad_centre=HEIGHT/2
    rpad_centre=HEIGHT/2
    lpad_vel=0
    rpad_vel=0
    spawn_ball(random.choice(['left', 'right']))

def draw(c):
    global lscore, rscore, ball_pos, ball_vel
    global lpad_centre, rpad_centre, lpad_vel, rpad_vel, pad_acc
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")

    c.draw_text(str(lscore), [(WIDTH/2) -60, 50], 50, 'Blue')
    c.draw_text(str(rscore), [(WIDTH/2) +30, 50], 50, 'Blue')
    
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # collide and reflect off left and right pads
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if ball_pos[1]+BALL_RADIUS>=lpad_centre-HALF_PAD_HEIGHT and ball_pos[1]-BALL_RADIUS<=lpad_centre+HALF_PAD_HEIGHT:
            ball_vel[0] = - (ball_vel[0]*ball_acc)
        else:
            rscore +=1
            spawn_ball('right')
        
    if ball_pos[0] > WIDTH-BALL_RADIUS-PAD_WIDTH:
        if ball_pos[1]+BALL_RADIUS>=rpad_centre-HALF_PAD_HEIGHT and ball_pos[1]-BALL_RADIUS<=rpad_centre+HALF_PAD_HEIGHT:
            ball_vel[0] = - (ball_vel[0]*ball_acc)
        else:
            lscore +=1
            spawn_ball('left')
    
    # Reflect from top and bottom
    if ball_pos[1] <= BALL_RADIUS:
       ball_vel[1] = - ball_vel[1]

    if ball_pos[1] > HEIGHT-1-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
            
    # draw paddles
    c.draw_polygon([(0, lpad_centre-HALF_PAD_HEIGHT), (0, lpad_centre+HALF_PAD_HEIGHT), (PAD_WIDTH, lpad_centre+HALF_PAD_HEIGHT), (PAD_WIDTH, lpad_centre-HALF_PAD_HEIGHT)], 1, 'White', 'White')
    c.draw_polygon([(WIDTH-PAD_WIDTH, rpad_centre-HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH, rpad_centre+HALF_PAD_HEIGHT), (WIDTH, rpad_centre+HALF_PAD_HEIGHT), (WIDTH, rpad_centre-HALF_PAD_HEIGHT)], 1, 'White', 'White')

    # update paddle's vertical position, keep paddle on the screen
    if ((not lpad_centre+lpad_vel <= HALF_PAD_HEIGHT) and (not lpad_centre+lpad_vel+HALF_PAD_HEIGHT >= HEIGHT)):
        lpad_centre += lpad_vel
    if ((not rpad_centre+rpad_vel <= HALF_PAD_HEIGHT) and (not rpad_centre+rpad_vel+HALF_PAD_HEIGHT >= HEIGHT)):
        rpad_centre += rpad_vel
        
def keydown(key):
    global HEIGHT, HALF_PAD_HEIGHT
    global lpad_vel, rpad_vel, lpad_centre, rpad_centre, pad_acc

    # Left pad movement
    if key == simplegui.KEY_MAP["w"]:
        lpad_vel -= pad_acc
    elif key == simplegui.KEY_MAP["s"]:
        lpad_vel += pad_acc

    # Right pad movement
    elif key == simplegui.KEY_MAP["up"]:
        rpad_vel -= pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        rpad_vel += pad_acc

def keyup(key):
    global lpad_vel, rpad_vel, lpad_centre, rpad_centre
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        lpad_vel = 0

    # Right pad movement
    elif key == simplegui.KEY_MAP["up"] or simplegui.KEY_MAP["down"]:
        rpad_vel = 0

def restart():
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Restart", restart, 100)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
