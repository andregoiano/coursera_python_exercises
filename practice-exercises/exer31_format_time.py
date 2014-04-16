# Define a function that returns formatted minutes and seconds

import time

###################################################
# Circle area formula
# Student should enter function on the next lines.

# define globals

m = " minutes"
s = " seconds"

# defne functions

def format_time(t):
    minutes = t / 60
    seconds = t % 60
    
    if t > 1 and t < 60:
        return str(seconds) + s
    elif t == 1:
        return str(seconds) + s[0:7]
    elif t == 60:
        return str(minutes) + m[0:7]
    elif t == 0:
        return "Time is zero"
    elif t > 60:
        return str(minutes) + m + " and " + str(seconds) + s
    else:
        return "Something's wrong"
    
###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)
print format_time(60)
print format_time(1)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds
