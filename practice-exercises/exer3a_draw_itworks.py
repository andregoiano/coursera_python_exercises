# Print to canvas

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw_something(canvas):
    canvas.draw_text("It works!", (120, 112), 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)

# 
frame.set_draw_handler(draw_something)

# starts frame
frame.start()
