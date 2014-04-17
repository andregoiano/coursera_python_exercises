# Counter ticks

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

# create timer
timer = simplegui.create_timer(interval, tick)

# start timer
timer.start()
