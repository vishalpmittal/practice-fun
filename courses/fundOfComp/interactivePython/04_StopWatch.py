# "Stopwatch: The Game"

# Import required libraries
import simplegui
import random
import math
import time

# define global variables
timer = None
total = 0
successes = 0

total_timer = 0
start_timer = 0
curr_timer = 0
print_timer = 0

t_msec = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def time_format(t):
    global t_msec
    t_sec = int(t)
    
    t_min = int(t_sec/60)
    t_sec = t_sec % 60
    
    t_sec_str = str(t_sec)
    if t_sec < 10:
        t_sec_str = '0' + t_sec_str
    t_msec = int((t-int(t)) * 10)
    return str(t_min) + ":" + t_sec_str + '.' + str(t_msec)

# event handlers for button: "Start"
def t_start():
    global total_timer, start_timer, curr_timer
    start_timer = time.time()
    timer.start()

# event handlers for button: "Stop"
def t_stop():
    global total, successes, t_msec, total_timer, start_timer, curr_timer
    check = timer.is_running()
    timer.stop()
    if check:    
        total += 1
        if t_msec == 0:
            successes += 1
    total_timer = curr_timer + total_timer

# event handlers for button: "Reset"
def t_reset():
    global total_timer, start_timer, curr_timer, total, successes, print_timer
    t_stop()
    total_timer = 0
    start_timer = 0
    curr_timer = 0
    print_timer = 0
    total = 0
    successes = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global total_timer, start_timer, curr_timer, print_timer
    curr_timer = time.time() - start_timer
    print_timer = curr_timer + total_timer

# define draw handler
def draw_handler(canvas):
    global total, successes, total_timer, start_timer, curr_timer, print_timer
    canvas.draw_text(str(successes) +'/' + str(total), (140, 30), 30, 'Green')
    canvas.draw_text(time_format(print_timer), (50, 110), 40, 'White')
                                                                
# create GUI frame
sw_frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)

# register event handlers for control elements
sw_frame.add_button("Start", t_start, 100)
sw_frame.add_button("Stop", t_stop, 100)
sw_frame.add_button("Reset", t_reset, 100)
sw_frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# start frame
sw_frame.start()
