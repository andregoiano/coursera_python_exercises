# template for "Stopwatch: The Game"

import simplegui

# define global variables

count = 0
number_of_stops = 0
winner_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

# def format(t):

def format(t):
    a = (t // 10)//60
    b = ((t // 10) % 60) // 10
    c = ((t // 10) % 60) % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

# define event handlers for buttons; "Start", "Stop", "Reset"

def start_handler():
    timer.start()
    
def stop_handler():
    global count, number_of_stops, winner_stops
    points = format(count)
    if timer.is_running():
        number_of_stops += 1
    if points[-1] == '0' and timer.is_running():
            winner_stops += 1
    timer.stop()
    
def reset_handler():
    global count, number_of_stops, winner_stops
    count = 0
    number_of_stops = 0
    winner_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global count
    count += 1
    
# define draw handler

# def draw():

def draw(frame):
    frame.draw_text(str(format(count)), (120, 150), 32, 'White')
    frame.draw_text("Stops: " + str(number_of_stops), (20, 30), 14, 'White')
    frame.draw_text("Points: " + str(winner_stops), (90, 30), 14, 'White')      
    
# create frame

frame = simplegui.create_frame("Stopwatch The Game", 300, 300)

# register event handlers

timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)

# buttons

start = frame.add_button("Start", start_handler, 100)
stop = frame.add_button("Stop", stop_handler, 100)
reset = frame.add_button("Reset", reset_handler, 100)

# start frame

frame.start()

# Please remember to review the grading rubric
