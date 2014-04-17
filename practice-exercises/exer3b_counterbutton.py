# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0
interval = 1000

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    

def reset_handler():
    global counter
    counter = 0
    timer.start()

def start_handler():
    timer.start()
    
def stop_handler():
    timer.stop()
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(interval, tick)

# add buttons to frame
reset = frame.add_button("Restart", reset_handler, 50)
start = frame.add_button("Start", start_handler, 50)
stop = frame.add_button("Stop", stop_handler, 50)

# Start timer
timer.start()
